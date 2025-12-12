from PIL import Image
import numpy as np
import os

# Basic Function
def readimage(img_name):
    global row,col
    im = Image.open(img_name)
    cimg = np.array(im)
    col,row = im.size
    return cimg,row,col

def intlimitimg(img2d):
    row,col=img2d.shape
    for i in range(row):
        for j in range(col):
            if img2d[i][j]>255:
                img2d[i][j]=255
            elif img2d[i][j]<0:
                img2d[i][j]=0
    return img2d

def color3dtogray2d(cimg,gimg):
    global row, col
    for i in range(row):
        for j in range(col):
            gimg[i][j] = int(0.299*cimg[i][j][0]+0.587*cimg[i][j][1]+0.114*cimg[i][j][2])

def intlimit(sum):
    if sum < 0 :
        sum *= -1
    elif sum > 255:
        sum = 255
    return sum

def maskfiltering2(img2d, maskx, masky):
    buff2d = img2d.copy()
    # global row, col
    row, col = img2d.shape
    ms = int(len(maskx) / 2)  # maskx and masky must be square with odd dimension.

    for i in range(ms, row - ms):
        for j in range(ms, col - ms):
            sumx = sumy = 0.0
            for p in range(-ms, ms + 1):
                for q in range(-ms, ms + 1):
                    sumx += buff2d[i + p][j + q] * maskx[p + ms][q + ms]
                    sumy += buff2d[i + p][j + q] * masky[p + ms][q + ms]
            img2d[i][j] = intlimit(abs(sumx) + abs(sumy))

smaskx=[[-1,0,1],[-2,0,2],[-1,0,1]]
smasky=[[-1,-2,-1],[0,0,0],[1,2,1]]

def mdc(inp, meanp): #inp is a single vector with a dimension of {dim}, and meanp is {cl} by {dim} matrix
    cl,dim = np.shape(meanp)
    dist = np.full(cl,0.0)
    mdist = 10**100  # initialization with a large value
    for i in range(cl):
        dist[i]=np.sqrt(np.sum(np.square(inp-meanp[i])))
        if dist[i] < mdist:
            mdist = dist[i]
            mcl = i

    return dist, mcl+1   # class number starts with not 0 but 1

o = []
p = []
o1 = []
p1 = []

input_folder = "./Project2_images"
image_files = os.listdir(input_folder)
for i in image_files:
    name = i
    cimg, row, col = readimage(f"{input_folder}/{i}")

    row, col = cimg.shape[0]//4, cimg.shape[1]//4
    cimg = cimg[2*cimg.shape[0]//4 : 3*cimg.shape[0]//4, 2*cimg.shape[1]//4 : 3*cimg.shape[1]//4 ]

    img = np.full((row, col), 0)
    # gray scaling & intlimit
    color3dtogray2d(cimg, img)
    intlimitimg(img)
    maskfiltering2(img, smaskx, smasky)

    x = np.std(img)
    if 'o' in name:
        # o.append(s)
        o1.append(x)
    elif 'p' in name:
        # p.append(s)
        p1.append(x)


om = [sum(o1)/len(o1)]
pm = [sum(p1)/len(p1)]
opm = np.array([om, pm])
print((om[0]+pm[0])//2)
print(o1)
print(p1)



test_folder = "./Test_images"
test_files = os.listdir(test_folder)

for t in test_files:
    cimg, row, col = readimage(f"{test_folder}/{t}")

    row, col = cimg.shape[0]//4, cimg.shape[1]//4
    cimg = cimg[2*cimg.shape[0]//4 : 3*cimg.shape[0]//4, 2*cimg.shape[1]//4 : 3*cimg.shape[1]//4 ]

    img = np.full((row, col), 0)
    color3dtogray2d(cimg, img)
    intlimitimg(img)
    maskfiltering2(img, smaskx, smasky)

    x = np.std(img)
    z = np.array([x])
    df, decide = mdc(z, opm)
    print(t)
    print(f"pattern {z} belongs to {decide} class by MDC {df}")
    print()

print(f"{sum(o1)/len(o1)}")
print(f"{sum(p1)/len(p1)}")