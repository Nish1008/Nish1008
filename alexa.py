import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
        
def Wishme():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("Good morning buddy!")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon buddy!")
        
    else:
        speak("good evening buddy!")  
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio ,language= 'en-in')
        print("user said:",query)
                
    except Exception as e:
       #print(e)
        
        
        print("say that again please......")
        return "None" 
    return query
        
if __name__ == '__main__':
    Wishme()
speak("i am alexa! how may i help you!")
while True:
    query = takeCommand().lower()
    
    
    if "wikipedia" in query:
        speak("searching for wikipedia.......")
        query = query.replace("wikipedia" , "")
        results = wikipedia .summary(query , sentences = 2)
        speak("according to wikipedia........")
        print(results)
        speak(results)
        
        
    elif "open google" in query:
        webbrowser.open("google.com")
        
    elif "open youtube" in query:
        webbrowser.open("youtube.com")   
        

    elif "open spotify "in query:
        webbrowser.open("spotify.com")
        
            

    
          
    
   
       
        
    