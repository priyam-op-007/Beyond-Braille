import speech_recognition as sr
from gtts import gTTS
import requests

def speech_to_text():
    # use microphone to listen to user's speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def text_to_speech(text):
    # convert text to speech using Google Text-to-Speech
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=False)
    filename = "text_to_speech.mp3"
    speech.save(filename)
    print(f"File saved as {filename}")

while True:
    # prompt user to speak and convert speech to text
    speech_text = speech_to_text()
    if speech_text:
        print(f"You said: {speech_text}")
    
    # prompt user to type a message and convert it to speech
    text = input("Type a message: ")
    if text:
        text_to_speech(text)
