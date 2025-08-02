
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")
    elif "date" in command:
        date_today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date_today}")
    elif "search" in command:
        speak("What should I search for?")
        query = get_audio()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("I didn’t quite get that. Could you repeat?")

speak("Hi! I'm your assistant. Say something.")
while True:
    command = get_audio()
    if command:
        process_command(command)
