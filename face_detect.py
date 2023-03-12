import cv2 as cv

img= cv.imread('Photos/photo_4.jpeg')
cv.imshow('Photo', img)
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

haar_cascade= cv.CascadeClassifier('Codes/haar_face.xml')

faces_rect= haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

print(f'Number of faces found= {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)