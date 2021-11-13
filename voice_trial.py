import speech_recognition as sr


l = sr.Recognizer()

with sr.Microphone() as source:
    print("listening")
    v = l.listen(source)
    text = l.recognize_google(v)
    print(text)