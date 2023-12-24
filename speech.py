import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)



# recognize speech using Whisper API
OPENAI_API_KEY = "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"
try:
    print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
except sr.RequestError as e:
    print("Could not request results from Whisper API")