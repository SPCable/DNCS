import cv2
import numpy as np
import dlib

def QuetKhuonMat(path):

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt.xml')
    i=0
    imax = 100
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.5,minNeighbors =2)
        for (x,y,w,h) in faces:
            if i<=imax:
                i=i+1

                roi_color = frame[y:y+h,x:x+h]

                item_pic = path + "\ " +str(i) + ".png"

                font = cv2.FONT_HERSHEY_SIMPLEX
                name = str(i)
                stroke = 2
                color = (255,255,255)
                cv2.putText(frame, name, (x,y),font,1,color,stroke,cv2.LINE_AA)

                color = (255,0,0)
                stroke = 2

                cv2.imwrite(item_pic,roi_color)
                endX = x + w
                endY = y + h  
                cv2.rectangle(frame,(x,y),(endX,endY),color,stroke)
            #khung hinh
        cv2.imshow('Quet khuon mat',frame)

        if cv2.waitKey(20) & 0xFF == ord('q') or i==imax:
            break
    cap.release()
    cv2.destroyAllWindows()
