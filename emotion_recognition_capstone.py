#Author: Abhishek Iyer & Srikrishna Narayanan
#This program gathers the emotional details using still images and a webcam by utilizing the "DEEPFACE" package

#Get Emotions on a Face from Photos
import cv2
#import emotions as emotions
from deepface import DeepFace
import numpy as np
import time

#img_path = 'face.jpg' #Storing the image into a variable called imagePath
#image = cv2.imread(img_path) #OpenCV method that loads the image from the specified file and stores it into image variable
#analyze = DeepFace.analyze(image) #The first input is the image we want to analyze; #The second input is the facial attribute analysis we perform, in this case we want to read emotions
#print(analyze['dominant_emotion'])

#Using webcam to collect emotion information

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
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

        detecting = DeepFace.analyze(frame, actions= ['emotion'])  # The first input is the image we want to analyze; #The second input is the facial attribute analysis we perform, in this case we want to read emotions
        print(detecting['dominant_emotion'])
        #cv2.putText(frame, 'sad', (x, y), font, 1, color, stroke, cv2.LINE_AA)
        #print("Error with emotion detection, please review code for any errors!")
    # cv2.imshow('gray', gray) #Displays a second frame in grayscale

    if detecting['dominant_emotion'] == 'happy':  #When the user's emotion is sad, then it triggers voice recognition
        pass
    elif detecting['dominant_emotion'] == 'neutral':
        pass
    else:
        from musicPlayer import lowerSong
        #from musicPlayer import VoiceRecog
        lowerSong()
        #time.sleep(2)
        import VoiceRecognition
        break
        #VoiceRecog()

    if cv2.waitKey(20) & 0xFF == ord('q'):  # Stops the frame/ allows us to close the current frame by hitting 'q'
        break  # This line and the above if statement is critical to show the actual camera in the frame, otherwise it will be gray and not respond!

# When everything is done, release the capture
captureDevice.release()
cv2.destroyAllWindows()

