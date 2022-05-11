#Author: Abhishek Iyer & Srikrishna Narayanan
#This program helps to create a music player in python that can pause, play, skip, and stop music
#(https://www.youtube.com/watch?v=D4B8omLT0zA)

import tkinter as tk #Used for the User Interface of the music player
import fnmatch
import os
from pygame import mixer

#Designing the user interface for our application
canvas = tk.Tk()
canvas.title("Music System") #Creating the title for our canvas
canvas.geometry("500x500") #Creating the dimensions/geometry for our system/canvas
canvas.config(bg = 'white') #Making the background (bg) color as white

root_path = 'C:\\Users\gayat\PycharmProjects\CapstoneProject2022\music' #This is path of where the music list is stored

#We only need to get the mp3 files from the folder and so we need to create a pattern that performs the matching
pattern = "*.mp3" #Looks for all the files with extension ".mp3"

mixer.init() #Initialize the mixer otherwise song will not play!
#Adding commands to buttons
def play(): #Defining a method for when the user clicks the play button
    label.config(text = listBox.get("anchor")) #Configuring the label to have the same name as the song in our list Box
    mixer.music.load(root_path + "\\" + listBox.get("anchor"))
    mixer.music.play() #Plays the song
    import emotion_recognition_capstone

def stop(): #Defining a method for when the user clicks the stop button
    mixer.music.stop() #Stops the current song
    listBox.select_clear('active') #This will deselect the active song after stopping it

def fastForward(): #Defining a method to skip to the next song
    next_song = listBox.curselection() #Returns the currently selected song
    next_song = next_song[0] + 1 #Gets the index of the current song and adds one to it to get the index of the next song
    next_song_name = listBox.get(next_song) #Gets the next song name
    label.config(text = next_song_name) #Adds the next song name to the label

    mixer.music.load(root_path + "\\" + next_song_name) #Loads the next song
    mixer.music.play()

    #Moves the cursor from the existing song to the next song
    listBox.select_clear(0, 'end') #The selection gets cleared
    listBox.activate(next_song) #Activates the hover for the next song
    listBox.select_set(next_song) #Passes the selection set once again


def previousRewind():
    prev_song = listBox.curselection() #Returns the currently selected song
    prev_song = prev_song[0] - 1 #Gets the index of the current song and subtracts one to it to get the index of the previous song
    prev_song_name = listBox.get(prev_song) #Gets the previous song name
    label.config(text = prev_song_name) #Adds the previous song name to the label

    mixer.music.load(root_path + "\\" + prev_song_name) #Loads the previous song
    mixer.music.play()

    #Moves the cursor from the existing song to the previous song
    listBox.select_clear(0, 'end') #The selection gets cleared
    listBox.activate(prev_song) #Activates the hover for the previous song
    listBox.select_set(prev_song) #Passes the selection set once again

#def haltMusic(): #Used to stop the music while the user records their voice

#def ResumeMusic(): #Continues the music after voice is recorded
    #mixer.music.unpause()

def pauseFunction(): #Defining a function to pause the song and need to use the conditionals to determine whether the song is currently paused
    if(pauseButton['text'] == "Pause"): #Checking to see if the the text of the Pause is clicked
        mixer.music.pause() #Pauses the current song
        pauseButton['text'] = 'Play' #Changing the pause button text to play
    else:
        mixer.music.unpause() #Unpauses the song
        pauseButton['text'] = 'Pause' #Changing the pause button text back to pause

def lowerSong():
    mixer.music.fadeout(4)

def leaveWindow():
    canvas.destroy()

#Shows the list of files within our User Interface using the "listbox" function within tkinter package
listBox = tk.Listbox(canvas, fg = 'red', bd = 5, bg = 'black', width = 100, font = ('timesnewroman', 12)) #Creating the listbox
listBox.pack(padx = 15, pady = 15) #Padding the listbox using the (x) and (y) coordinates

#Trying to add items to our list box
#listbox.insert(0, "Coding") #Adding the title "Coding" into the 0th index/place of our listBox
#listbox.insert(1, "Writing") #Adding the title "Writing" into the 1st index/place of our listBox
#listbox.insert(2, "Reading") #Adding the title "Reading" into the 2nd index/place of our listBox

#Adding label to our music player/system
label = tk.Label(canvas, text = '', bg = 'white', fg = 'green', font = ('timesnewroman, 14'))
label.pack(padx = 20, pady = 20)

#Create a new frame to store the buttons in horizontal order
top = tk.Frame(canvas, bg = 'white')
top.pack(padx = 20, pady = 10, anchor = 'center') #anchor allows the buttons to appear in a specific position of the screen

#Adding a few buttons to control our music player
previousButton = tk.Button(canvas, text = "Previous", command = previousRewind)
previousButton.pack(pady = 15, in_ = top, side = 'left') #Stores the button that come after this to the left side

stopButton = tk.Button(canvas, text = 'Stop', command = stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play", command = play)
playButton.pack(pady = 15, in_ = top, side = 'left')

forwardButton = tk.Button(canvas, text = 'Forward', command = fastForward)
forwardButton.pack(pady = 15, in_ = top, side = 'right') #Stores the button that come after this to the right side

pauseButton = tk.Button(canvas, text = 'Pause', command = pauseFunction)
pauseButton.pack(pady = 15, in_ = top, side = 'right')

closeButton = tk.Button(canvas, text = 'Close Window', command = leaveWindow)
closeButton.pack(pady = 20)

lowerVolume = tk.Button(canvas, text = 'Reduce Volume', command = lowerSong)
lowerVolume.pack(pady = 15)


#Searching for songs to put in the listBox
for root, dirs, files in os.walk(root_path): #Traverse through the path for all directories, roots, and files
    for filename in fnmatch.filter(files, pattern): #Match all the files with the pattern
        listBox.insert('end', filename) #"end" adds the files from the path at the end and name will be filename

def VoiceRecog():
    import VoiceRecognition

canvas.mainloop()
