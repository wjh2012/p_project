import requests
from bs4 import BeautifulSoup

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1699389")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

sizeTable = infoSoup.find('table', {'class':'table_th_grey'})

try:
    trs = sizeTable.tbody.find_all('tr',{'class':None, 'id':None})

    print(trs)

    for tr in trs:
        print(len(tr.text.strip().split()))
        print(tr.text.strip())
        print('\n')


except AttributeError as e:
    print('error')
