import requests
from bs4 import BeautifulSoup
import re
import json

def getInfo(pantsID):

    def is_digit(str):
        try:
            tmp = float(str)
            return True
        except ValueError:
            return False

    pantsInfo = requests.get("https://store.musinsa.com/app/goods/"+str(pantsID))
    infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

    # name(제품명)
    name = infoSoup.find('em',{'class':None, 'id':None}).text.strip()

    # category(카테고리)
    category = infoSoup.find('p',{'class':'item_categories'}).text.strip().split('>')[1].split()[0]

    # popular(만족도)
    pop = infoSoup.find('span',{'class':'rate'})
    popu = pop.text.split('%')[0]

    if is_digit(popu):
        popular = popu
    else:
        popular = "0"
        

    # sales(후기 수)
    sell = infoSoup.find('a',{'href':'#estimateBox'})    
    try:
        numList = re.findall("\d+",sell.text)
        strNum =""
        for i in range(len(numList)):
            strNum = strNum+numList[i]
        sales = strNum
    except AttributeError as e:
        sales='0'

    # img(이미지 링크)
    img = infoSoup.find('div', {'class':'product-img'}).find('img').attrs['src']

    # price(가격)
    cost = infoSoup.find('span',{'class':'product_article_price'})
    numList = re.findall("\d+",cost.text.strip())
    strNum =""
    for i in range(len(numList)):
        strNum = strNum+numList[i]
    price = strNum

    # sex(성별)
    s = infoSoup.find('span', {'class':'txt_gender'})
    se= s.text.strip()
    if '남'in se and '여' in se:
        sex = 'a'
    elif '남' in se:
        sex = 'm'
    elif '여' in se:
        sex = 'f'

    pantsDic = {
        'id':pantsID,
        'name':name,
        'category':category,
        'popular':popular,
        'sales' : sales,
        'img':img,
        'price':price,
        'sex':sex
    }
            
    return (pantsDic)
