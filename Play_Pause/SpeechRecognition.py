# Python program to translate
# speech to text and text to speech
 
# importing the libraries
from bs4 import BeautifulSoup
import requests
import speech_recognition as sr
import pyttsx3
import subprocess
import sys
 
# Initialize the recognizer
r = sr.Recognizer()

# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     

# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            SpeakText("sir, how may i help you ")
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText == 'nothing for now':
                SpeakText("Ok sir ")
                break
            
            if MyText == 'pause':
                SpeakText("Pausing the video sir")
                p = subprocess.Popen(['powershell.exe', 'C:\\Users\\divya\\OneDrive\\Desktop\\space.ps1'], stdout=sys.stdout) 
                p.communicate()
          
            if MyText == 'play':
                SpeakText("Playing the video sir")
                p = subprocess.Popen(['powershell.exe', 'C:\\Users\\divya\\OneDrive\\Desktop\\space.ps1'], stdout=sys.stdout) 
                p.communicate()
            
            else:
                print("Did you say ",MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")