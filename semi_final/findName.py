import requests
from bs4 import BeautifulSoup

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

name = infoSoup.find('em',{'class':None, 'id':None})
print(name.text.strip())