from tkinter import *
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import openai

root = Tk()
root.title("GPT-3 Alexa")
root.geometry("200x100")

# Authenticate to the OpenAI API and set the API key

openai.api_key = "Your_OpenAi_API"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def run_gpt(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

def run_alexa():
    command = take_command()
    response = run_gpt(command)
    talk(response)

# Create a button to start the script
start_button = Button(root, text="Start", command=run_alexa)
start_button.pack()

# Add the last update date to the script
last_update = Label(root, text=f"Last Update: {datetime.now().date()}")
last_update.pack()

root.mainloop()
