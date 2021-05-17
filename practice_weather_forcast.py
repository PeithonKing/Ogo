import Modules.WeatherForcast.WeatherForcast as wf 
place = "Kolkata"
weather = wf.forecast(place)
# print(weather)

'''weather={'date': '2021-02-27',
 'day': {'humidity': None,				##############
         'narrative': None,
         'phrases': None,				##############
         'precipitate': None,			##############
         'temperature': None,			##############
         'uv_description': None,
         'wind_speed': None},
 'night': {'humidity': 83,				##############
           'narrative': 'Generally clear. Hazy. Low 21ºC. Winds SSW at 10 to '
                        '15 km/h.',
           'phrases': 'Mostly Clear',	##############
           'precipitate': None,			##############
           'temperature': 21,			##############
           'uv_description': 'Low',
           'wind_speed': 12},
 'place': 'Kolkata',
 'time': '23:22:31'}'''

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
if weather['day']['wind_speed']:
	day += "\tWind Speed: " + str(weather['day']['wind_speed']) + "\n"

night = ""
if weather['night']['phrases']:
	night += "\tWeather: " + weather['night']['phrases'] + "\n"
if weather['night']['temperature']:
	night += "\tTemperature: " + str(weather['night']['temperature']) + "\n"
if weather['night']['precipitate']:
	night += "\tPrecipitation: " + str(weather['night']['precipitate']) + "\n"
if weather['night']['humidity']:
	night += "\tHumidity: " + str(weather['night']['humidity']) + "\n"
if weather['night']['wind_speed']:
	night += "\tWind Speed: " + str(weather['night']['wind_speed']) + "\n"


print(intro)
print("Day :" + day)
print("Night :" + night)


