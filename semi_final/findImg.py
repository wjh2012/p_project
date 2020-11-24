import requests
from bs4 import BeautifulSoup

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

Img = infoSoup.find('div', {'class':'product-img'})

Link = Img.find('img').attrs['src']

print(Link)