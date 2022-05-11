#Author: Abhishek Iyer & Srikrishna Narayanan
#This file is used to train the Facial Recognition Model
import os
from PIL import Image
import numpy as np
import cv2 #OpenCV
import pickle

from numpy import size

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
#smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')
#profile_face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create() #Our Recognizer

#Walking through the directory looking for PNG or JPEG files to train
Base_Directive = os.path.dirname(os.path.abspath(__file__)) #Looking for the directory of the python file
image_directory = os.path.join(Base_Directive, "Images") #Looking for the directory containing the images

currentLabel_id = 0
label_ids = {} #We are creating an empty dictionary to store the label ids
y_label = []
x_train = []

#Want to see the images in the directory/files
for root, directives, files in os.walk(image_directory):
    for file in files: #Iterates through the files
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file) #Prints the path of the file
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower() #Used in case filename was mislabeled
            #label = os.path.basename(root).replace(" ", "-").lower()  # Shows that the filename can be obtained by root
            #print(label, path) #Printing out file path
            if not label in label_ids:
                #pass #If the label is in the dictionary, then we will set the id into the dictionary
                #If not in the dictionary, then we will add the label in the dictionary and add the current id number
                 label_ids[label] = currentLabel_id
                 currentLabel_id += 1
            identification = label_ids[label]
            #print(label_ids)
            #y_label.append(label) #While this is an intuitive solution, we would want to use a number for our label
            #x_train.append(path) #We also want to verify this image and turn it into a NUMPY Array and convert to grayscale much like Cascade

            #Training Image to NumPy Array
            pil_image = Image.open(path).convert("L") #Gives us an image of the path and .convert("L") turns into grayscale

            #Resize the image for training (Causing Tuple Index Out of Range ISSUE!!!) - Need to fix
            #size(600,600)
            #final_image = pil_image.resize(size, Image.ANTIALIAS)

            image_array = np.array(pil_image, "uint8") #Converting it into a NumPy Array by taking every pixel value and turning it into an NumPy Array
            #print(image_array) #Prints out the image that we converted into an array of numbers

            #Region of Interest in Training Data
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5) #Doing the face detection inside the image
            #smiles = smile_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            #profileFace = profile_face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for (x,y,w,h) in faces:
                roiImage = image_array[y:y+h, x:x+w]
                x_train.append(roiImage)
                #We have the region of interest, but we need a label for the image!
                #We know the labels, but do not have a number value associated with the label

            #Creating Training Labels!
                y_label.append(identification)


    #print(y_label)
    #print(x_train)

    #Using Pickle to Save Ids
with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f) #Dumps the Label Ids of each image into the file

    #Train the OpenCV Recognizer
recognizer.train(x_train, np.array(y_label)) #Inputs the region of interest of the training data and converts the y_labels as an numpy array
recognizer.save("trainer.yml")



