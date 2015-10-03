#!/usr/bin/python

import datetime
from feedgen.feed import FeedGenerator
from pushbullet import Pushbullet

from check import Aurora


url = 'http://www.aurora-service.eu/aurora-forecast/'
kpThreshold = 5
alertList = Aurora(url, kpThreshold).getAlertList()

today = datetime.date.today()

description = ''
for item in alertList:
	title = item[0].strftime('%d/%m/%Y') + ': ' + item[1] + '-' + item[2]
	description	+= title + " - kp" + str(item[3]) + "\n"


if len(alertList) > 0:
	pbKey = '7962b1649658b184a9ecfb78844f7384'
	pb = Pushbullet(pbKey)
	push = pb.push_note("Aurora status over kp" + str(kpThreshold), description)
