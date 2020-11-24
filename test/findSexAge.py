import requests
from bs4 import BeautifulSoup
import re

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

age = infoSoup.find('span', {'class':'prd_like_cnt'})

print(age)