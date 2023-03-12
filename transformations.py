import cv2 as cv
import numpy as np

img=cv.imread('Photos/photo_3.jpeg')
cv.imshow('Photo', img)

# Translation
def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down
#translated= translate(img, 100, 100)
translated= translate(img, -100, -300)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint= None):
    (height, width)= img.shape[:2]
    if(rotPoint== None):
        rotPoint=(width//2, height//2)
    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, rotMat, dimensions)
rotated= rotate(img, 45)
cv.imshow('Rotated', rotated)
rotated_rotated= rotate(rotated, 45)
cv.imshow('Rotated rotated', rotated_rotated)
rotated_cumulative= rotate(img, 90)
cv.imshow('Rotated cumulative', rotated_cumulative)

# Resizing

resized= cv.resize(img , (750,750), interpolation= cv.INTER_AREA)
cv.imshow('Resized', resized )

# Flipping
flipped= cv.flip(img, -1)
cv.imshow(' Flipped', flipped)

# Cropping
cropped= img[200:400, 300:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)  
