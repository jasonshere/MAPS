import cv2
import os
import time

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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
#    k = cv2.waitKey(1000)

#    if k%256 == 27:
#        # ESC pressed
#        print("Escape hit, closing...")
#        break
#        #elif k%256 == 32:
#    elif k == -1:
        # SPACE pressed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        img_name = "{}/{:04}.jpg".format(folder,img_counter)
        cv2.imwrite(img_name, frame[y:y+h,x:x+w])
        print("{} written!".format(img_name))
        img_counter += 1
cam.release()
cv2.destroyAllWindows()
