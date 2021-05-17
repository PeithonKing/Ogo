import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import Modules.WeatherForcast.WeatherForcast as wf 
# import Modules.alarm.alarm


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
		intro = "Weather forcast for " + weather['place'] + " for " + weather['date'] + " is"
		day = ""
		if weather['day']['phrases']:
			day += "\tWeather: " + weather['day']['phrases'] + "\n"
		if weather['day']['temperature']:
			day += "\tTemperature: " + str(weather['day']['temperature']) + "\n"
		if weather['day']['precipitate']:
			day += "\tPrecipitation: " + str(weather['day']['precipitate']) + "\n"
		if weather['day']['humidity']:
			day += "\tHumidity: " + str(weather['day']['humidity']) + "\n"

		night = ""
		if weather['night']['phrases']:
			night += "\tWeather: " + weather['night']['phrases'] + "\n"
		if weather['night']['temperature']:
			night += "\tTemperature: " + str(weather['night']['temperature']) + "\n"
		if weather['night']['precipitate']:
			night += "\tPrecipitation: " + str(weather['night']['precipitate']) + "\n"
		if weather['night']['humidity']:
			night += "\tHumidity: " + str(weather['night']['humidity']) + "\n"
			
		speak(intro)
		speak("Day :" + day)
		speak("Night :" + night)
		
	
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
