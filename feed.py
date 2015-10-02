#!/usr/bin/python

from check import Aurora

url = 'http://www.aurora-service.eu/aurora-forecast/'
alertList = Aurora(url, 5).getAlertList()
print(alertList)


