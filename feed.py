#!/usr/bin/python3.4

import datetime
import sys
import configparser
from feedgen.feed import FeedGenerator
from pushbullet import Pushbullet

from checker import AuroraChecker

config = configparser.ConfigParser()
config.read('config.ini')

url = config['DEFAULT']['AuroraURL']
pbKey = config['DEFAULT']['PushbulletKey']
kpThreshold = config['DEFAULT']['KpThreshold']


if not url and not pbKey and not kpThreshold:
	sys.exit("ERROR reading config.ini, please read documentation.")

if not kpThreshold.isdigit():
	sys.exit("ERROR reading kpThreshold, integer required.")
else:
	kpThreshold = int(kpThreshold)

alertList = AuroraChecker(url, kpThreshold).getAlertList()
pb = Pushbullet(pbKey)


if not isinstance(alertList, list):
	pb.push_note("WARNING: Aurora-service.eu is down", "Aurora-service.eu is down and the checker has not been able to correctly update.")
else:
	today = datetime.date.today()
	utcTime = datetime.datetime.utcnow()

	description = ''
	for item in alertList:
		title = item[0].strftime('%d/%m/%Y') + ': ' + "UTC" + item[1] + '-' + item[2]
		description	+= title + " - kp" + str(item[3]) + "\n"

	if len(alertList) > 0:
		title = "Aurora status over kp" + str(kpThreshold) + " at UTC " + utcTime.strftime("%H:%M")
		pb_channel = pb.channels[0]
		print(description)
		pb_channel.push_note(title, description)

with open('log.txt', 'a') as file:
    file.write('Successfully run at ' + datetime.datetime.now().strftime("%x - %H:%M") + "\n")
