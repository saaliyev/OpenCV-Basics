import cv2 as cv

img=cv.imread('Photos/photo_3.jpeg')
cv.imshow('Photo', img)

# Averaging
average= cv.blur(img , (3,3))
cv.imshow('Average blur', average)

# Gaussian Blur
gaussian= cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian blur', gaussian)

# Median Blur
median= cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral
bilateral= cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
