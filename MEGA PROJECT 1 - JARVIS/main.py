import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
import study_material as sm
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
 
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")

def speak(text):
    engine = pyttsx3.init()
    engine.stop()
    engine.say(text)#add text to queue
    engine.runAndWait()#processes queue and makes the computer actually speak
    
def aiProcesses(command):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
        )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command},
        ]
    )
    return completion.choices[0].message.content  

def tellTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def tellDate():
    now = datetime.now()
    current_date = now.strftime("%d%B%Y")
    return current_date

def processCommand(command):
    if "music" in command.lower():
        webbrowser.open("https://www.youtube.com/watch?v=gkSO4JmJ8L4&list=RDgkSO4JmJ8L4&start_radio=1")  
    elif "open github" in command.lower():
        webbrowser.open("https://github.com")  
    elif "open google" in command.lower():
        webbrowser.open("https://google.com")  
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")  
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
        
    elif "time" in command.lower():
        current_time = tellTime()
        speak(f"The current time is {current_time}")
        
    elif "date" in command.lower():
        current_date = tellDate()
        speak(f"The current date is {current_date}")
        
    elif command.lower().startswith("play"):
        video = command.lower().split(" ")[1]#important
        link = sm.material[video]
        webbrowser.open(link) 
               
    elif "news" in command.lower():
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        print(req.status_code)
        print(req.text)
        if req.status_code == 200:
            data = req.json()
            articles = data["articles"]
            for article in articles:
                speak(article["title"])
    
    else:
        # If nothing work, then we make openAI handle the requests  
            output = aiProcesses(command)  
            speak(output )

if __name__ == "__main__":
    r = sr.Recognizer()
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake up word 'Jarvis'
        # Obtain audio from the microphone
        print("recognizing...")    
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
            #for offline speech recognition use sphinx
            # word = r.recognize_sphinx(audio)
            word = r.recognize_google(audio)#internet connection require for recognition
            print("Wake word : ",word)
            if "jarvis" in word.lower():
                speak("hnji katoch ji")  
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command received: {command}")
                    processCommand(command)
            elif "exit" in word.lower() or "quit" in word.lower() or "stop" in word.lower():
                speak("Goodbye!")
                break        
                 
        except Exception as e:
            print(f"Error : {e}")         
                 
            
            