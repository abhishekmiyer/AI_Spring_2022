#Author: Abhishek Iyer & Srikrishna Narayanan
#This program makes use of webcam and OPENCV to record the user's face and identify the name based on trained data
import numpy as np #Optional import
import cv2 #OpenCV
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

#Creating a random String containing the keyword "sad"
#systemKeyWord = 'sad'

#Recognizing eyes and smile
#eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create() #Our Recognizer
recognizer.read("trainer.yml") #Bringing in our trained data

labelDictionary = {}
    #Using Pickle to Save Ids
with open("labels.pickle", 'rb') as f: #rb = read bytes, wb = write bytes
    og_labelDictionary = pickle.load(f) #Dumps the Label Ids of each image into the file
    labelDictionary = {v:k for k,v in og_labelDictionary.items()} #We are inverting the format of person_name : 1 into 1 : person_name



captureDevice = cv2.VideoCapture(0) #Creating a device called captureDevice which will access the webcam

while True:#Loop made for continuous usage of the video
    ret, frame = captureDevice.read() #Reading every single frame in our video capture
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cvtColor = Convert Color #Blue Green Red by default
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for(x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #region of interest as grayscale
                   #(ycoord_start, ycoord_end) , (xcoord_start, xcoord_end) Taking into account Height and Width
        roi_color = frame[y:y+h, x:x+w] #region of interest as color using the "frame"
        img_item = "my-image.png" #Save face
        cv2.imwrite(img_item, roi_gray) #Save just a portion of face and remove everything else

        #Drawing the rectangle around the face or also known as region of interest
        color = (255, 0, 0) #BGR = 255 (Completely Blue)
        stroke = 5
        width = x + w #end_coord_x
        height = y + h #end_ccord_y
        cv2.rectangle(frame, (x,y), (width, height), color, stroke) #(x,y) are the starting coordinates

        #Using eye cascade to iterate through the image to find eyes
        #eyes = eye_cascade.detectMultiScale(roi_gray) #Finding the eyes by iterating through the image
        #for(ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0,), 5,) #Putting a frame around the eyes

        #Using smile cascade to iterate through the image to find smile
        #smiles = smile_cascade.detectMultiScale(roi_gray)
        #for(sx, sy, sw, sh) in smiles:
            #cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0,0,255), 5) #Putting a frame for smiles


        #RECOGNIZER? (Start Video at 44:26) (https://www.youtube.com/watch?v=PmZ29Vta7Vc)
        currentlabel_id, confidence = recognizer.predict(roi_gray) #We are predicting a region of interest in grayscale and assigning a label and confidence level
        if confidence >= 45 and confidence <= 85: #This is not the best model, so confidence levels need to be adjusted
            print(currentlabel_id) #This assigns a training label, but we do not have an id (aka the name of the person) associated with the image/video
            #We need to load our labels from the "pickle package"
            print(labelDictionary[currentlabel_id])

            #OpenCV PutText allows us to put the label on the image itself
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labelDictionary[currentlabel_id]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

        #if labelDictionary[currentlabel_id] == 'sad':
                #import VoiceRecognition

    cv2.imshow('frame', frame)  # Displays the frame
    #cv2.imshow('gray', gray) #Displays a second frame in grayscale

    if cv2.waitKey(20) & 0xFF == ord('q'): #Stops the frame/ allows us to close the current frame by hitting 'q'
            break #This line and the above if statement is critical to show the actual camera in the frame, otherwise it will be gray and not respond!

#When everything is done, release the capture
captureDevice.release()
cv2.destroyAllWindows()

