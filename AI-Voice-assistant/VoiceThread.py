import speech_recognition as sr
import pyttsx3
import threading

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to listen to audio input
def listen_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Error making request to Google Speech Recognition service; {0}".format(e))

# Example usage
while True:
    text = listen_audio()
    print("You said: " + text)
    if "hello" in text:
        threading.Thread(target=speak_text, args=("Hello, how can I help you?",)).start()
    elif "goodbye" in text:
        threading.Thread(target=speak_text, args=("Goodbye, have a nice day!",)).start()
        break
