from urllib.request import urlopen

url = 'http://www.aurora-service.eu/aurora-forecast/'
response = urlopen(url)
html = response.read()
print(html)

