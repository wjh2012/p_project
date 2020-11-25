import requests
from bs4 import BeautifulSoup
import json

import page_id
pageList = page_id.IDParser()

def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False

for pants in pageList[0]:
    pantsInfo = requests.get("https://store.musinsa.com/app/goods/"+str(pants))
    infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

    # 사이즈 테이블
    sizeTable = infoSoup.find('table', {'class':'table_th_grey'})

    try:
        trs = sizeTable.tbody.find_all('tr',{'class':None, 'id':None})

        for tr in trs:
            if len(tr.text.strip().split()) < 6:
                raise AttributeError        
            
            length = tr.text.split()[1]
            waist = tr.text.split()[2]
            thigh = tr.text.split()[3]
            rise = tr.text.split()[4]
            hem = tr.text.split()[5]

            if is_digit(length) and is_digit(waist) and is_digit(thigh) and is_digit(rise) and is_digit(hem):
                sizeDic = {
                    'id':pants,
                    'length':length,
                    'waist':waist,
                    'thigh':thigh,
                    'rise':rise,
                    'hem':hem
                }

                json_data = json.dumps(sizeDic,ensure_ascii=False)

            else:
                raise AttributeError            

            print(json_data)

    except AttributeError as e1:
        print(pants+' e1 None')
