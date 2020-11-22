import requests
from bs4 import BeautifulSoup

url = 'https://lirik.kapanlagi.com/artis/naif/di-mana-aku-di-sini/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

judul = soup.find('h5')
print(judul.text)
lirik = soup.findAll('span', 'lirik_line')
for lyric in lirik:
	lrk = lyric.text
	print(lrk)
