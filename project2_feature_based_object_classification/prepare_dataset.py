import os,time
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

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

def writeimage2d(img,name):
    row,col = img.shape
    intlimitimg(img)
    img=np.uint8(img)
    im=Image.fromarray(img)
    im.save(name)
    return im

# region growing



# classifier
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




# Implement (train)
input_folder = "./Project2_images"
output_folder = "./Test_images"
image_files = os.listdir(input_folder)
o = 1
for i in image_files:
    print(f"{input_folder}/{i}")
    # read
    cimg, row, col = readimage(f"{input_folder}/{i}")
    gimg2d = np.full((row,col),0)
    # gray scaling & intlimit
    color3dtogray2d(cimg,gimg2d)
    intlimitimg(gimg2d)
    # save
    writeimage2d(gimg2d,f"train{o}.png")
    o+=1







'''
# Implement
# read
cimg, row, col = readimage("o1.png")
gimg2d = np.full((row,col),0)
# gray scaling
color3dtogray2d(cimg,gimg2d)


# save
writeimage2d(gimg2d,"test.png")
'''