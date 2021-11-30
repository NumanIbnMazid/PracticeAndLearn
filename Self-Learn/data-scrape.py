from bs4 import BeautifulSoup
import requests


url = "http://www.imdb.com/chart/top"

resp = requests.get(url)

# print(resp)

soup = BeautifulSoup(resp.text)

# print(soup)

llist = soup.find('tbody', {'class':'lister-list'})

trs = llist.findAll('tr')

result = []

for tr in trs:
    name = tr.find('td', {'class':'titleColumn'}).text
    print(name)
    result.append(name)
    
with open('imdb.txt', 'w') as outfile:
    outfile.write('/n'.join(result))
