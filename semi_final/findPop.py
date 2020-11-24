import requests
from bs4 import BeautifulSoup
import re

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1698571")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

pop = infoSoup.find('a',{'href':'#estimateBox'})

## 값이 없는 경우 에러처리 및 None 반환
try:
    numList = re.findall("\d+",pop.text)

    strNum =""

    for i in range(len(numList)):
        strNum = strNum+numList[i]

    print(strNum)
except AttributeError as e:
    print("None")
