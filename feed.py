#!/usr/bin/python

import datetime
from feedgen.feed import FeedGenerator
from pushbullet import Pushbullet

from check import Aurora


url = 'http://www.aurora-service.eu/aurora-forecast/'
kpThreshold = 6
alertList = Aurora(url, kpThreshold).getAlertList()

today = datetime.date.today()

description = ''
for item in alertList:
	title = item[0].strftime('%d/%m/%Y') + ': ' + "UTC" + item[1] + '-' + item[2]
	description	+= title + " - kp" + str(item[3]) + "\n"

utcTime = datetime.datetime.utcnow()

if len(alertList) > 0:
	pbKey = '7962b1649658b184a9ecfb78844f7384'
	pb = Pushbullet(pbKey)
	text = "Aurora status over kp" + str(kpThreshold) + " at UTC " + utcTime.strftime("%H:%M")
	pb_channel = pb.channels[0]
	pb_channel.push_note(text, description)
