import os, time
import datetime
from playsound import playsound

alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = str(input("am or pm? "))


if amPm == "pm":
		alarmH = alarmH + 12
while True:
	os.system('cls')
	hour = datetime.datetime.now().hour
	minute = datetime.datetime.now().minute
	second = datetime.datetime.now().second
	if (alarmM - minute - 1) >= 0:
		print("Waiting for alarm: " + str(alarmH - hour) + " Hr " + str(alarmM - minute - 1) + " Min " + str(59 - second) + " sec ")
		time.sleep(1)
	os.system('cls')
	if(alarmH == hour and alarmM == minute):
		print("Time to wake up!")
		playsound('beep 1.mpeg')
		break
