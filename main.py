import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
r=sr.Recognizer()

def record_audio(ask= False):
    with sr.Microphone() as source:
        if ask:
            ami_speak(ask)
        audio=r.listen(source)
        voice_data=""
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            ami_speak('Sorry,I did not get that')
        except sr.sr.RequestError:
            ami_speak("Sorry, my speech service is down")
        return voice_data

def ami_speak(audio_string):
    tts= gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file ='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        ami_speak('My name is Amisha')
    if 'what time is it' in voice_data:
        ami_speak(time.ctime())
    if 'search' in voice_data:
        search=record_audio('What do you want to search for?')
        url='https://google.com/search?q=' +search
        webbrowser.get().open(url)
        ami_speak("Here is what i found for "+search)
    if 'find location' in voice_data:
        location=record_audio('What location do you want to find?')
        url='https://google.nl/maps/place/' +location+"/&amp;"
        webbrowser.get().open(url)
        ami_speak("Here is the location of "+location)
    if "exit" in voice_data:
        exit()
    if 'go to class' in voice_data:
        url='http://eclass.srv.ualberta.ca/'
        webbrowser.get().open(url)
        ami_speak("Here is the E-class page")
        
time.sleep(1)
ami_speak('How can I help you?')
while 1:
    voice_data=record_audio()
    respond(voice_data)
