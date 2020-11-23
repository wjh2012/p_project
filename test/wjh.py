import requests
from bs4 import BeautifulSoup

# 바지 카테고리
html = requests.get("https://search.musinsa.com/category/003")

soup = BeautifulSoup(html.content, "html.parser")

# 총 페이지 수
result = soup.find('span',class_= 'totalPagingNum')
total_page = int(result.text)

# 요청할 페이지 목록
link_doc = []
for i in range(1, total_page+1):
    link_doc.append("https://search.musinsa.com/category/003?device=&d_cat_cd=003&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page="+str(i)+"&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q=")

for t in link_doc:
    print(t)
