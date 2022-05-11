#Author: Abhishek Iyer & Srikrishna Narayanan
from deepface import DeepFace
import cv2
import time
from deepface.basemodels import VGGFace, OpenFace, Facenet, FbDeepFace, DeepID
model = VGGFace.loadModel()

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
import json
from deepface.extendedmodels import Emotion
models = {}
models["emotion"] = Emotion.loadModel()
captureDevice = cv2.VideoCapture(0) #Creating a device called captureDevice which will access the webcam
while True:#Loop made for continuous usage of the video
    ret, frame = captureDevice.read() #Reading every single frame in our video capture
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cvtColor = Convert Color #Blue Green Red by default
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        # print(x,y,w,h)
        roi_gray = gray[y:y + h, x:x + w]  # region of interest as grayscale
        # (ycoord_start, ycoord_end) , (xcoord_start, xcoord_end) Taking into account Height and Width
        roi_color = frame[y:y + h, x:x + w]  # region of interest as color using the "frame"
        img_item = "my-image.png"  # Save face
        cv2.imwrite(img_item, roi_gray)  # Save just a portion of face and remove everything else

        # Drawing the rectangle around the face or also known as region of interest
        color = (255, 0, 0)  # BGR = 255 (Completely Blue)
        stroke = 5
        font = cv2.FONT_HERSHEY_SIMPLEX
        width = x + w  # end_coord_x
        height = y + h  # end_coord_y
        cv2.rectangle(frame, (x, y), (width, height), color, stroke)  # (x,y) are the starting coordinates

        cv2.imshow('frame', frame)  # Displays the frame
        time.sleep(3)

DeepFace.analyze(" ", models=models)


