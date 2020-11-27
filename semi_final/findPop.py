import requests
from bs4 import BeautifulSoup
import re

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

pop = infoSoup.find('span',{'class':'rate'})

print(pop.text.split('%')[0])