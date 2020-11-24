import requests
from bs4 import BeautifulSoup
import re

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

sales = infoSoup.find('strong',{'id':'sales_1y_qty'})

print(sales)