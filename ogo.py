import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from Modules import WeatherForcast as wf 


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(text):
	print(text)
	engine.say(text)
	engine.runAndWait()


def input():
	try:
		with sr.Microphone() as source:
			speak('\nlistening...')
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command = command.lower()
			if 'ogo' in command:
				command = command.replace('ogo', '')
	except:
		pass
	return command


def RunOgo():
	command = input()
	print(command)
	
	if 'play' in command:
		song = command.replace('play', '')
		speak('playing ' + song)
		pywhatkit.playonyt(song.strip())
		
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%I:%M %p')
		speak('Current time is ' + time)
		
	elif 'who is' in command or 'wikipedia' in command:
		if 'who is' in command:	
			command = command.replace('who is', '')
		if "search" in command:
			command = command.replace('search', '')	
		if "wikipedia" in command:
			command = command.replace('wikipedia', '')
		info = wikipedia.summary(command.strip(), 1)
		print(info)
		speak(info)
		
	elif 'date' in command:
		speak('Sorry! I have a headache!')
		
		
	elif "marry" in command or "love" in command:
		speak("That's Nice, but I really like our relationship the way it is!")
				
	elif 'joke' in command:
		speak(pyjokes.get_joke())
		
	# Work is going on in weather forecast!
	elif 'weather' in command:
		speak("Please repeat only the name of the place!")
		place = input()
		weather = wf.forecast(place)
		tell = ""
		for key, value in weather['night'].items():
			if value:
				tell+= "bash"
			else: print("\t\tNo value for " + key)
		
	
	else:		
		if "google" in command:
			command = command.replace('google', '')
		if "search the web for" in command:
			command = command.replace('search the web for', '')	
		if "search for" in command:
			command = command.replace('search for', '')
		if "search" in command:
			command = command.replace('search', '')
		if "for" in command:
			command = command.replace('for', '')
		if "web" in command:
			command = command.replace('web', '')
		if "what is" in command:
			command = command.replace('what is', '')			
		speak('Searching the web for ' + '"' + command.strip() + '"')
		pywhatkit.search(command)


RunOgo()
