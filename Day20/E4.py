# 4. UCI is one of the most common places to get data sets for data science and machine learning.
#   Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
#   Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'cellpadding': '5'})
rows = table.findAll('tr')

data = []
for row in rows:
    cols = row.findAll('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

print(data[:2])
