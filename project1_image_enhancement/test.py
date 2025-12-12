import numpy as np
from PIL import Image


# Basic Function
def readimage(img_name):
    global row,col
    im = Image.open(img_name)
    cimg = np.array(im)
    col,row = im.size
    return cimg,row,col

def limit2d(arr2d,minv,maxv):
    row,col = arr2d.shape
    for i in range(row):
        for j in range(col):
            if arr2d[i][j]>maxv:
                arr2d[i][j]=maxv
            elif arr2d[i][j]<minv:
                arr2d[i][j]=minv
    return arr2d

def saveimage2d(img,name):
    row,col = img.shape
    limit2d(img, 0 , 255) # 원래 limit2d(img)
    img=np.uint8(img)
    im=Image.fromarray(img)
    im.save(name)
    return im

# Data Scaling Function
# z_standardization
def z_standard(gimg2d):
    buff2d = np.full((row, col), 0.0)

    mean = gimg2d.mean()
    std = gimg2d.std()

    buff2d[:, :] = (gimg2d[:, :] - mean) / std

    # Keeping about 95%
    minv = -1.96
    maxv = 1.96
    limit2d(buff2d, minv, maxv)
    buff2d = mmn2dimg(buff2d, minv, maxv)

    return buff2d

# minmax normalization (minv -> 0, maxv -> 작을수록 밝기 올라간다.)
def mmn2dimg(gimg2d, minv, maxv):
    # minv=min(map(min,gimg2d))
    # maxv=max(map(max,gimg2d))
    buff2d = np.full((row, col), 0.0)

    if minv < 0:
        gimg2d = gimg2d[:, :] - minv
        maxv = maxv - minv
        minv = 0.0

    buff2d[:, :] = 255.0 * (gimg2d[:, :] - minv) / (maxv - minv)
    buff2d = np.round(buff2d)
    return buff2d

def histoeq(gimg2d):
    buff2d = np.full((row,col),0)
    histo = np.full(256,0)
    pdf=np.full(256,0.0)
    cdf=np.full(256,0.0)

    for i in range(row):
        for j in range(col):
            histo[gimg2d[i][j]] +=1

    for i in range(256):
        pdf[i] = histo[i]/(row*col)
        if i==0:
            cdf[i] = pdf[i]
        else:
            cdf[i] = cdf[i - 1] + pdf[i]

    for i in range(row):
        for j in range(col):
            buff2d[i][j]=round(255.0*cdf[gimg2d[i][j]])

    return buff2d


# intlimit
def intlimit(sum):
    if sum < 0 :
        sum *= -1
    elif sum > 255:
        sum = 255
    return sum

# Filtering Function
def maskfiltering(img2d, mask):
    buff2d = img2d.copy()
    row, col = img2d.shape
    ms = int(len(mask) / 2)  # mask must be square with odd dimension.

    for i in range(ms, row - ms):
        for j in range(ms, col - ms):
            sum = 0.0
            for p in range(-ms, ms + 1):
                for q in range(-ms, ms + 1):
                    sum += buff2d[i + p][j + q] * mask[p + ms][q + ms]
            img2d[i][j] = intlimit(sum)


def medianfiltering(img2d, ms):
    buff2d = img2d.copy()
    row, col = img2d.shape
    hs = int(ms / 2)  # mask must be square with odd dimension.

    for i in range(hs, row - hs):
        for j in range(hs, col - hs):
            temp = []
            for p in range(-hs, hs + 1):
                for q in range(-hs, hs + 1):
                    temp.append(buff2d[i + p][j + q])
            temp.sort()
            img2d[i][j] = temp[int(ms * ms / 2)]

# Implement
# read
cimg, row, col = readimage("clock_noise1.png")
gimg2d = np.full((row,col),0)
# gray scaling
gimg2d[:,:] = 0.299*cimg[:,:,0]+0.587*cimg[:,:,1]+0.114*cimg[:,:,2]

# standardization
gimg2d = z_standard(gimg2d)

# normalization
gimg2d = mmn2dimg(gimg2d, 0, 125)
# generate gaussian mask
msize = 3
gmask = np.zeros((msize, msize))
std = 2.0
hs=int(msize/2)
for i in range(-hs,hs+1):
    for j in range(-hs,hs+1):
        gmask[i+hs][j+hs] = (1.5/hs)*(1.0/(2*3.1416*std))*np.exp(-1.0*(i*i+j*j)/(2*std*std))
# filtering

maskfiltering(gimg2d, gmask)
maskfiltering(gimg2d, gmask)

# save
saveimage2d(gimg2d, "test.png")


