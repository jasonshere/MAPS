import cv2
import os
import time

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
cv2.namedWindow("record images")

img_counter = 0
name = input("Enter name: ")
folder = './dataset/{}'.format(name)
if not os.path.exists(folder):
    os.makedirs(folder)

while img_counter < 10:
    ret, frame = cam.read()
    cv2.imshow("MAPS", frame)
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smileCascade.detectMultiScale(roi_gray, scaleFactor= 1.5, minNeighbors=15, minSize=(25, 25))
        
        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)
            img_name = "{}/{:04}.jpg".format(folder,img_counter)
            cv2.imwrite(img_name, frame[y:y+h,x:x+w])
            print("{} written!".format(img_name))
            img_counter += 1
cam.release()
cv2.destroyAllWindows()
