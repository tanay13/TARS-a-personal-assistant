import pyttsx3
import datetime

import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Tars , How may i help you?")
    

def takeCommand():
    #It takes microphone input from user and gives string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: {query}\n" )
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    takeCommand()