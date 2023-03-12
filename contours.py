import cv2 as cv
import numpy as np

img=cv.imread('Photos/photo_1.jpeg')
cv.imshow('Photo', img)

blank= np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
gray= cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
blurred= cv.GaussianBlur(img, (5,5), cv. BORDER_DEFAULT)
cv.imshow('Blurred', blurred)
canny= cv.Canny(blurred, 125, 175)
cv.imshow('Canny Edges', canny)
#contours, hierarchy= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
ret, thresh= cv.threshold(gray, 125, 255, cv. THRESH_BINARY)
cv.imshow('Thresh', thresh)
contours, hierarchy= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)