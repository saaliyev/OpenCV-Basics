import cv2 as cv
# rescaleFrame function in rescale_photo.py and rescale_video.py are the same. I tested this function in separate files for the sake of simplicity.

def rescaleFrame(frame, scale=0.75):
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimesions= (width, height)
    return cv.resize(frame, dimesions, interpolation= cv.INTER_AREA)

capture= cv.VideoCapture('Videos/video1.mov')

while True:
    isTrue, frame= capture.read()
    frame_resized= rescaleFrame(frame)
    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()