from Modules import WeatherForcast as wf 
place = "Bhubaneswar"
weather=wf.forecast(place)
#print(weather)

'''weather={'date': '2021-02-27',
 'day': {'humidity': None,
         'narrative': None,
         'phrases': None,
         'precipitate': None,
         'temperature': None,
         'uv_description': None,
         'wind_speed': None},
 'night': {'humidity': 83,
           'narrative': 'Generally clear. Hazy. Low 21ºC. Winds SSW at 10 to '
                        '15 km/h.',
           'phrases': 'Mostly Clear',
           'precipitate': None,
           'temperature': 21,
           'uv_description': 'Low',
           'wind_speed': 12},
 'place': 'Kolkata',
 'time': '23:22:31'}'''
'''
narrative = weather['night']['narrative'].split(".")
print(narrative)
n=0
for word in narrative:
	narrative[n]=narrative[n].strip()
	n+=1
	if word == "":
		narrative.remove(word)
print(narrative)'''

tell = ""
for key, value in weather['night'].items():
	if value:
		if key == "narrative":
			narrative = value.split(".")
			n=0
			for word in narrative:
				narrative[n]=narrative[n].strip()
				n+=1
				if word == "":
					narrative.remove(word)
print(narrative)			
'''				if n==0:
					tell += "The sky will remain " + narrative[n]
				else:
					tell += "not in " + str(n) + ". "
'''
tell += "The sky will remain " + narrative[0] + ".\n"
if " " not in narrative[1]:
	tell += "Distant visibility will be " + narrative[1] + ".\n"
else:
	pass
print(tell)

