import requests
from bs4 import BeautifulSoup
import re

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

price = infoSoup.find('span',{'class':'product_article_price'})

numList = re.findall("\d+",price.text.strip())

strNum =""

for i in range(len(numList)):
    strNum = strNum+numList[i]

print(strNum)