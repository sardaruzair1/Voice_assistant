import pyttsx3
import speech_recognition as spr
import datetime
import pyjokes
import webbrowser
import pyaudio
def sptext():
    recognizer = spr.Recognizer()
    with spr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio_data  = recognizer.listen(source)
        print("recognining...")
        data = recognizer.recognize_google(audio_data)
        try:
            print(data)
        except spr.UnknownValueError:
            print(" Not Understand")    
                
sptext()    