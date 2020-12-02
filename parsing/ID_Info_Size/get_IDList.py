import requests
from bs4 import BeautifulSoup

def IDParser():
    # 바지 카테고리
    pants = requests.get("https://search.musinsa.com/category/003")

    pantsSoup = BeautifulSoup(pants.content, "html.parser")

    # 총 페이지 수
    pageFind = pantsSoup.find('span',class_= 'totalPagingNum')
    totalPage = int(pageFind.text)
    print("totalpage is ",totalPage)

    page = [] # 이중 리스트로 구현
    # pantsLinkList 하나씩 접근 후 페이지마다 ID 크롤링

    for i in range(2):
        pantsLink = "https://search.musinsa.com/category/003?device=&d_cat_cd=003&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page="+str(i+1)+"&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q="

        IDList = []

        pantsID = requests.get(pantsLink)
        IDSoup = BeautifulSoup(pantsID.content, "html.parser")

        IDBox = IDSoup.findAll('li', {'class':'li_box'}) 

        for ID in IDBox:
            if 'data-no' in ID.attrs:
                IDList.append(ID.attrs['data-no'])

        page.append(IDList)
        print("page ",i+1," ID crawling complete")

    return page