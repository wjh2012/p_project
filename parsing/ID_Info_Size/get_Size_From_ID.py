import requests
from bs4 import BeautifulSoup
import json

def getSize(pantsID):
    pantsInfo = requests.get("https://store.musinsa.com/app/goods/"+str(pantsID))
    infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

    findTable = infoSoup.find('table', {'class':'table_th_grey'})
    
    if findTable is not None:
        # 사이즈 테이블
        sizeTable = findTable.tbody.find_all('tr')

        sizeListList = []

        for tr in sizeTable:            
            result = tr.find_all('td',{'class':'goods_size_val'})
            
            if result:
                sizeList =[]

                for size in result:
                    sizeList.append(size.text)
                
                if len(sizeList)>4:
                    sizeDic = {
                        'id':pantsID,
                        'length':sizeList[0],
                        'waist':sizeList[1],
                        'thigh':sizeList[2],
                        'rise':sizeList[3],
                        'hem':sizeList[4]
                    }
                    sizeListList.append(sizeDic)
        
        return sizeListList
