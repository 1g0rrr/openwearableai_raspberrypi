import speech_recognition as sr
import os
from io import BytesIO
from openai import OpenAI
from gpiozero import Button
from signal import pause

# obtain audio from the microphone
r = sr.Recognizer()

def say_hello():
    print("Hello!")
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Whisper API
    OPENAI_API_KEY = "--"
    client = OpenAI(api_key=OPENAI_API_KEY)

        
    wav_data = BytesIO(audio.get_wav_data())
    wav_data.name = "SpeechRecognition_audio.wav"

    transcript = client.audio.transcriptions.create(model="whisper-1", file=wav_data, response_format="text")
    print(transcript)

button = Button(2)

button.when_pressed = say_hello

pause()

# try:
#     print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
# except sr.RequestError as e:
#     print("Could not request results from Whisper API")