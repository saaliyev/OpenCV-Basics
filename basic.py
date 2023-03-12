import cv2 as cv

img= cv.imread('Photos/photo_1.jpeg')
cv.imshow('View', img)
#converting to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur= cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
canny= cv.Canny(blur, 125, 175)
cv.imshow('Blurred Canny Edges', canny)


# Dilating the image
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

# Eroding 
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized=cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('resized', resized)
# for shrinking use INTER_AREA
# for enlarging use INTER_LINEAR
# INTER_CUBIC is the slowest but with most quality

# Cropping
cropped= img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)