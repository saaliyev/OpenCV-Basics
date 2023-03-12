import cv2 as cv

img= cv.imread('Photos/photo_1.jpeg')
cv.imshow('Photo', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Simple thresholding
threshold ,thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)
threshold ,thresh_inv= cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold inverse', thresh_inv)

# Adaptive thresholding
adaptive_thresh= cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv. THRESH_BINARY, 11, 3)
cv.imshow('Adaptive threshold', adaptive_thresh)
cv.waitKey(0)