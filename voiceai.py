#CREATE AI ASSISTNT LIKE HER AND JARVICEs 

import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
#import pyaudio

engine=pyttsx3.init()

#below code changes voice

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#1=FEMALE
#0=MALE
newVoiceRate=199
engine.setProperty('rate',newVoiceRate)

#below function convert text to speach
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#below function is for time
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("current time is")
    speak(Time)

#below function is for date
def date():
    Date=datetime.datetime.now().strftime("%d/%m/%Y")
    speak("current date is")
    speak(Date)

#Wish me
def wishme():
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening") 
    else:
        speak("good night")   
def takeCommand():
    speak("How can I help you! Say in English Loudly")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 #wait for 1 second
        audio= r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_ibm(audio, 'en=US')#'en=IN' for indian english. 'en=US' for US english
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry! Due TO slow internet I didn't understand  that ....")
        
        return "None"

    return query



wishme()
speak("hello! this is AI assistant ")    
time()
date()
takeCommand()

