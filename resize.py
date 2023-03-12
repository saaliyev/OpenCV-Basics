import cv2 as cv

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture= cv.VideoCapture(0)
print(cv.CAP_PROP_FRAME_WIDTH)
print(cv.CAP_PROP_FRAME_HEIGHT)
changeRes(1000,1000)
print(cv.CAP_PROP_FRAME_WIDTH)
print(cv.CAP_PROP_FRAME_HEIGHT)
while True:
    isTrue, frame= capture.read()
    cv.imshow('video', frame)

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()