import requests
from bs4 import BeautifulSoup

html = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

soup = BeautifulSoup(html.text, "html.parser")

result = soup.find_all("div", class_="tit3")

for t in result:
    print(t.text.strip())
