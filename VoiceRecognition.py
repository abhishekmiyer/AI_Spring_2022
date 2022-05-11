#Author: Abhishek Iyer & Srikrishna Narayanan
#This program test audio output using various packages and also records the user's voice and stores in text file
#Using playsound to play audio (Only performs playback)
#from playsound import playsound
#playsound('C:\\Users\gayat\PycharmProjects\CapstoneProject2022\\AudioFileOne.mp3')

#Using simpleaudio to play audio (Only uses .wav file as input)
#import simpleaudio as sa
#filename = 'DavidSo.wav'
#wave_obj = sa.WaveObject.from_wave_file(filename)
#play_obj = wave_obj.play()
#play_obj.wait_done() #Wait until sound has finished playing and mandatory to hear audio else audio does not play

#Using simpleaudio and NumPy array to play audio
#import numpy as np
#import simpleaudio as sa
#frequency = 300 #Note will be played at 440 Hz
#fs = 44100 #Number of samples per second
#seconds = 3 #Note duration of 3 seconds
#t = np.linspace(0, seconds, seconds * fs, False) #Generating an array from 0 to seconds in seconds * fs increments
#note = np.sin(frequency * t * 2 * np.pi) #Generating a 440 Hz sine wave
#audio = note * (2**15 - 1) / np.max(np.abs(note)) # Ensuring that the highest value is 16 bit
#audio =  audio.astype(np.int16) #Convert to 16-bit data
#play_obj = sa.play_buffer(audio, 1, 2, fs) #Start playback
#play_obj.wait_done() #Wait until sound has finished playing and mandatory to hear audio else audio does not play

#------------------------------------------------------------------------------------------------------
#Recording audio using python-sounddevice
#import sounddevice as sd
#import wavio
#import soundfile as sf
#from numpy import int16, uint8
#from scipy.io.wavfile import write

#fs = 10000 #Sample rate
#seconds = 1 #Duration of recording

#myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=2)
#sd.wait() # Wait until recording is finished
#wavio.write('talk.wav', myrecording, fs, sampwidth=2)
#data, fs = sf.read('talk.wav') #Extracting audio data and sampling rate from file
#sf.write('talk.flac', data, fs)
#---------------------------------------------------------------------------------------------------------
#import speech_recognition as sr
#voice = sr.AudioFile('talk.flac')
#r = sr.Recognizer()
#with voice as source:
    #try:
        #r.adjust_for_ambient_noise(source)
        #audio_data = r.record(source, duration=3)
        #text = r.recognize_google(audio_data)
        #print(text)
    #except sr.UnknownValueError:
        #print("Audio is not transcribed. Please use a different file!")
#-----------------------------------------------------------------------------------------------------------

#from musicPlayer import lowerVolume
#lowerVolume()

#Using simpleaudio to play audio (Only uses .wav file as input)
import time

import simpleaudio as sa
filename = 'RecordVoice.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done() #Wait until sound has finished playing and mandatory to hear audio else audio does not play

import speech_recognition as sr
mic = sr.Microphone()
r = sr.Recognizer()
with mic as source:
    r.adjust_for_ambient_noise(source, duration=2)
    audio = r.listen(source, phrase_time_limit=0.5)
    outfile = open('data.txt', 'w')
    text = r.recognize_google(audio)
    outfile.write(text)
    outfile.close()
    print(text)


#from musicPlayer import stop
#from musicPlayer import fastForward
#fileResponse = open('data.txt', 'r') #Reading the data file and storing the user's response into the variable fileResponse

#if(fileResponse == 'yes'):
    #fastForward()














