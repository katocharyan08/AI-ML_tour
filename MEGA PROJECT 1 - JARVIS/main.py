import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init() 
    
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
                 
            
            