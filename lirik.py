import requests
from bs4 import BeautifulSoup
import time

judul = input("input: ")
url = 'https://www.google.com/search?q=lirik {}&ie=UTF-8'  .format(judul)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

print(url)
req = requests.get(url, headers=headers)
print(req)
soup = BeautifulSoup(req.text, 'html.parser')

judul = soup.find('h2', 'qrShPb kno-ecr-pt PZPZlf mfMhoc')
artis = soup.find('div', 'wwUB2c PZPZlf')
print('Judul :', judul.text)
print('Artis :', artis.text)
lirik = soup.findAll('span', {'jsname':'YS01Ge'})
for lyric in lirik:
	lrk = lyric.text
	print(lrk)
