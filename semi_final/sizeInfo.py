import requests
from bs4 import BeautifulSoup

pantsInfo = requests.get("https://store.musinsa.com/app/goods/1149328")
infoSoup = BeautifulSoup(pantsInfo.content, "html.parser")

sizeTable = infoSoup.find('table', {'class':'table_th_grey'})

trs = sizeTable.tbody.find_all('tr',{'class':None, 'id':None})

for tr in trs:
    print(tr.text.strip())
    print('\n')
