import requests
from bs4 import BeautifulSoup

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

graph = infoSoup.find_all('span', {'class':'bar_num'})

print(graph)