import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
import study_material as sm


engine = pyttsx3.init() 
newsapi = "4b8412eb8d304172941735b03f38e190"
    
def speak(text):
    engine.say(text)#add text to queue
    engine.runAndWait()#processes queue and makes the computer actually speak

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")  
    elif "open github" in command.lower():
        webbrowser.open("https://github.com")  
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")  
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
        video = command.lower().split(" ")[1]#important
        link = sm.material[video]
        webbrowser.open(link)    
    elif "news" in command.lower():
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if req.status_code == 200:
            data = req.json()
            articles = data["articles"]
            for article in articles:
                speak(article["title"])
                

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
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            #for offline speech recognition use sphinx
            # word = r.recognize_sphinx(audio)
            word = r.recognize_google(audio)#internet connection require for recognition
            if word.lower() == "jarvis" or word.lower() == "hey jarvis":
                speak("hnji katoch ji")  
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command received: {command}")
                    
                    processCommand(command)
                 
        except Exception as e:
            print(f"Error : {e}")         
                 
            
            