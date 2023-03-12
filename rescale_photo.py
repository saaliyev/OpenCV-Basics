import cv2 as cv
# rescaleFrame function in rescale_photo.py and rescale_video.py are the same. I tested this function in separate files for the sake of simplicity.

def rescaleFrame(frame, scale=0.75):
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimesions= (width, height)
    return cv.resize(frame, dimesions, interpolation= cv.INTER_AREA)

img= cv.imread('Photos/photo_1.jpeg')
resized_img= rescaleFrame(img)
cv.imshow('Photo', img)
cv.imshow('Resized photo', resized_img)
cv.waitKey(0)