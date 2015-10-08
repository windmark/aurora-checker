#!/usr/bin/python

import datetime
import configparser
from feedgen.feed import FeedGenerator
from pushbullet import Pushbullet

from check import AuroraChecker

config = configparser.ConfigParser()
config.read('config.ini')

url = config['DEFAULT']['AuroraURL']
kpThreshold = int(config['DEFAULT']['KpThreshold'])
pbKey = config['DEFAULT']['PushbulletKey']

alertList = AuroraChecker(url, kpThreshold).getAlertList()

today = datetime.date.today()
utcTime = datetime.datetime.utcnow()

description = ''
for item in alertList:
	title = item[0].strftime('%d/%m/%Y') + ': ' + "UTC" + item[1] + '-' + item[2]
	description	+= title + " - kp" + str(item[3]) + "\n"

if len(alertList) > 0:
	pb = Pushbullet(pbKey)
	title = "Aurora status over kp" + str(kpThreshold) + " at UTC " + utcTime.strftime("%H:%M")
	pb_channel = pb.channels[0]
	print(description)
	#pb_channel.push_note(title description)
