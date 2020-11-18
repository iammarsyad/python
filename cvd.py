import json
from urllib import request

url = "https://data.covid19.go.id/public/api/prov.json"


response = request.urlopen(url)

data = json.loads(response.read())

for covid in data['list_data']:
	print(f"- {covid['key']}:")
	print(f"  🤒Positif: {covid['jumlah_kasus']}")
# r = requests.get(url)

# data = r.json()
# print(data)

# headers = {
# 	'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:83.0) Gecko/20100101 Firefox/83.0.'
# }


# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'html.parser')
# items = soup.findAll('div', 'col-md-3')

# print(items)