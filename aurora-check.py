from urllib.request import urlopen
from bs4 import BeautifulSoup
from dateutil.parser import parse
import re

url = 'http://www.aurora-service.eu/aurora-forecast/'
response = urlopen(url)
html = response.read()
#print(html)

soup = BeautifulSoup(html, 'html.parser')
unformatedTable = soup.find_all('pre')[0].get_text()
tableList = unformatedTable.replace(" ", "").split('\n')

unformatedDates = tableList.pop(0)
dateLength = 5
formatedDates = [unformatedDates[i:i+dateLength] for i in range(0, len(unformatedDates), dateLength)]
for obj in enumerate(formatedDates, start=0):
	formatedDates[obj[0]] = parse(obj[1])


kpThreshold = 6
alertList = list()


forecastInfo = list()
for data in tableList:
	if data:
		unformated = data.split('UT')
		hours = unformated[0].split('-')
		values = re.findall('.', unformated[1])
		info = hours[0], hours[1], values
		forecastInfo.append(info)

		for kp in values:
			if int(kp) > kpThreshold:
				alertList.append(info)


print(alertList)