import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World! This is just a bit of text to verify whether or not this is working correctly.")
    engine.runAndWait()
    engine.stop()