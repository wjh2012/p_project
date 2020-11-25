import requests
from bs4 import BeautifulSoup
import re

pantsInfo = requests.get("https://store.musinsa.com/app/goods/658030")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

s = infoSoup.find('span', {'class':'txt_gender'})
se= s.text.strip()
if '남'and'여' in se:
    sex = 'a'
elif '남' in se:
    sex = 'm'
elif '여' in se:
    sex = 'f'
print(se)
print(sex)