#libraries used
import cv2
import numpy as np

#trained model
trainedfacemodel=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

#capture our face
webcam=cv2.VideoCapture(0)
while True:
    workingcorrectly,video=webcam.read()
    blacknwhite=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)#convert coloured image into black&white
    face=trainedfacemodel.detectMultiScale(blacknwhite)
    i=0
    for (x,y,w,h) in face:
        cv2.rectangle(video,(x,y),(x+w,y+h),(0,225,0),10)
        i=i+1
        cv2.putText(video,'face num'+str(i),(x-w,y-w),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
    cv2.imshow("shafi",video)
    key=cv2.waitKey(1)
    if key==27:#to close the webcam use esc key
        webcam.release()
        cv2.destroyAllWindows()
        break
    print(i)