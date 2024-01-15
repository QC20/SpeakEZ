'''
See for inspo; 
https://www.youtube.com/watch?v=MnYwCurv54c&ab_channel=Tommy%27sCodebase

'''import pyttsx3
import speech_recognition as sr
import openai
import env



# openai KEY
openai.api_key = env.OPEN_AI_KEY

# Initialize the speech engine
engine = pyttsx3.init(driverName='sapi5')  # Specify the driverName

def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()

#init speech recognizer

rec =sr.Recognizer()
speak('Hello I am here to answer your requests')

with sr.Microphone() as source:
    audio = rec.listen(source)
    speak('I am thinking for a moment..')


test = rec.recognize_google(audio)

discussion = openai.Completion.create(
    prompt=text,
    engine='text-davinci-002',
    max_tokens=1000,
)

answer = discussion
print(answer)