import speech_recognition as sr
import openai
import gtts
import wave
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import pyaudio

# initialize recognizer class (for recognizing the speech)


# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# openai api key
openai.api_key = "YOUR_API_KEY"

# initialize the plot
fig, ax = plt.subplots()
p = pyaudio.PyAudio()
sample_size = p.get_sample_size(pyaudio.paInt16)

def animate(i):
    with sr.Microphone() as source:
        # get audio data
        audio_data = r.listen(source)
    # update the plot
    raw_data = audio_data.get_raw_data()
    x = np.arange(0, len(raw_data))
    line, = ax.plot(x, np.frombuffer(raw_data, np.int16))

# start the animation
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()



# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using google speech recognition
    text = r.recognize_google(audio_text)
    print("Text: " + text)
    # pass the text to OpenAI
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text
    )
    print("OpenAI says: " + response["choices"][0]["text"])
    # convert the response text to speech
    tts = gtts.gTTS(response["choices"][0]["text"])
    tts.save("response.mp3")
    # play the response speech
    chunk = 1024  
    wf = wave.open("response.mp3", 'rb')  
    p = pyaudio.PyAudio()  

        # open stream
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),  
                channels = wf.getnchannels(),  
                rate = wf.getframerate(),  
                output = True)  

    # read data
    data = wf.readframes(chunk)  

    # play stream
    while data:  
        stream.write(data)  
        data = wf.readframes(chunk)  

    # stop stream
    stream.stop_stream()  
    stream.close()  

    # close PyAudio
    p.terminate() 
    print("Response played out from speaker")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except sr.UnknownValueError:
    print("Sorry, I did not get that")

