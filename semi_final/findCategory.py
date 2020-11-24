import requests
from bs4 import BeautifulSoup

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1699676")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

category = infoSoup.find('p',{'class':'item_categories'})
print(category.text.strip().split('>'))