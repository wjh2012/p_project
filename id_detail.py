import requests
from bs4 import BeautifulSoup
import re
import json

import page_id
pageList = page_id.IDParser()

for pants in pageList[0]:
    pantsInfo = requests.get("https://store.musinsa.com/app/goods/"+str(pants))
    infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

    # name(제품명)
    name = infoSoup.find('em',{'class':None, 'id':None}).text.strip()

    # category(카테고리)
    category = infoSoup.find('p',{'class':'item_categories'}).text.strip().split('>')[1].split()[0]

    # popular(후기)
    pop = infoSoup.find('a',{'href':'#estimateBox'})    
    try:
        numList = re.findall("\d+",pop.text)
        strNum =""
        for i in range(len(numList)):
            strNum = strNum+numList[i]
        popular = strNum
    except AttributeError as e:
        popular='0'

    # img(이미지 링크)
    img = infoSoup.find('div', {'class':'product-img'}).find('img').attrs['src']

    # price(가격)
    cost = infoSoup.find('span',{'class':'product_article_price'})
    numList = re.findall("\d+",cost.text.strip())
    strNum =""
    for i in range(len(numList)):
        strNum = strNum+numList[i]

    price = strNum

    pantsDic = {
        'id':pants,
        'name':name,
        'category':category,
        'popular':popular,
        #'sales'못가져옴
        'img':img,
        'price':price
        #'sex' 못가져옴
        #'age' 못가져옴
    }

    json_data = json.dumps(pantsDic,ensure_ascii=False)
    
    print(json_data)
