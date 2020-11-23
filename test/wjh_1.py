import requests
from bs4 import BeautifulSoup

html = requests.get("https://search.musinsa.com/category/003?device=&d_cat_cd=003&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page=1&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q=")

soup = BeautifulSoup(html.content, "html.parser")

result = soup.select('ul', {'id':'searchList'})

print(result)