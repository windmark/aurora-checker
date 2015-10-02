#!/usr/bin/python

from urllib.request import urlopen
from bs4 import BeautifulSoup
from dateutil.parser import parse
import re



class Aurora:
	url = ''
	kpThreshold = 0

	def __init__(self, url, kpThreshold):
		self.url = url
		self.kpThreshold = kpThreshold


	def getAlertList(self):
		response = urlopen(self.url)
		html = response.read()

		soup = BeautifulSoup(html, 'html.parser')
		unformatedTable = soup.find_all('pre')[0].get_text()
		tableList = unformatedTable.replace(" ", "").split('\n')

		unformatedDates = tableList.pop(0)
		dateLength = 5
		formatedDates = [unformatedDates[i:i+dateLength] for i in range(0, len(unformatedDates), dateLength)]
		for obj in enumerate(formatedDates, start = 0):
			formatedDates[obj[0]] = parse(obj[1])

		alertList = list()
		forecastList = list()

		for data in tableList:
			if data:
				data = re.sub(r'\([^)]*\)', '', data)
				unformated = data.split('UT')
				hours = unformated[0].split('-')
				values = re.findall('.', unformated[1])
				
				for obj in enumerate(values, start = 0):
					kp = int(obj[1])
					forecast = formatedDates[obj[0]], hours[0], hours[1], kp
					forecastList.append(forecast)

					if kp >= self.kpThreshold:
						alertList.append(forecast)
		alertList.sort()
		return(alertList)

		
