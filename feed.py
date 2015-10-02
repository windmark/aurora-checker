#!/usr/bin/python

import datetime
from feedgen.feed import FeedGenerator
from check import Aurora


url = 'http://www.aurora-service.eu/aurora-forecast/'
alertList = Aurora(url, 5).getAlertList()

today = datetime.date.today()

feedGen = FeedGenerator()
feedGen.id('http://windmark.se/aurora.rss')
feedGen.title('Aurora RSS')
feedGen.author( {'name':'Marcus Windmark','email':'marcus@windmark.se'} )
feedGen.link( href='http://windmark.se/aurora', rel='alternate' )
feedGen.language('en')
feedGen.description('The latest Aurora new from aurora-service.eu')

description = ''
for item in alertList:
	title = item[0].strftime('%d/%m/%Y') + ': ' + item[1] + '-' + item[2]
	description	+= title + "\n"


print(description)
feedEntry = feedGen.add_entry()
feedEntry.id('1')
feedEntry.title('Aurora Status ' + today.strftime('%d/%m/%Y'))
feedEntry.content(description)
feedGen.rss_file('rss.xml', pretty=True)