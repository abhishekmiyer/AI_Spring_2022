# Author: Abhishek Iyer & Srikrishna Narayanan
#This program identifies faces in a given image and draws a blue rectangle around the user's face
#Importing Revelant Modules
import PIL.Image
import PIL.ImageDraw
import face_recognition #Package used to recognize a face in a given image
#The PIL package/module is what will allow us to take an image and draw specific boxes around the faces

#-----------------------------------

#Let us start by inputting an image and get Python to recognize it!

picture = face_recognition.load_image_file('Classmates.jpg') #Loads the given image
#print(picture) #Stores the "blueprint" of the image as a series of arrays/matrices of numbers
face_locator = face_recognition.face_locations(picture)
print(face_locator) #Returns an array with coordinates of the located face (top, right, bottom, left)

#--------------------------------------------------------

#We can get Python to print how many faces it recognizes

how_many_faces = len(face_locator)
#print(how_many_faces) #Returns the number of faces in the image
print("Python located {} face(s) in this image".format(how_many_faces)) #Take the value of howManyFaces and puts in bracket

#-------------------------------------------

#Get Python to draw rectangles around the images

pil_picture = PIL.Image.fromarray(picture) #Apply the PIL Image to find the image
#pil_picture.show() #Shows the inputted image
draw_picture = PIL.ImageDraw.Draw(pil_picture) #Allows us to draw on the given image

for faces in face_locator: #Runs through each tuple/conmbination in the array
    top, right, bottom, left = faces #Assigns each location to the respective location in the picture
    draw_picture.rectangle([right, bottom, left, top], outline = "blue", width = 10)

pil_picture.show()
