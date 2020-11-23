import pandas as pd
from bs4 import BeautifulSoup
import requests

req = requests.get(
    "http://openapi.seoul.go.kr:8088/6a53646e71776a683636547a475663/xml/RealtimeCityAir/1/100"
)

sample = req.text

soup = BeautifulSoup(sample, "html.parser")

time = soup.select("MSRDT")
district = soup.select("MSRSTE_NM")
microdust = soup.select("PM10")
nanodust = soup.select("PM25")

timelist = []
districtlist = []
microdustlist = []
nanodustlist = []

for tmp in time:
    t = f"{tmp.text[:4]}년 {tmp.text[4:6]}월 {tmp.text[6:8]}일 {tmp.text[8:10]}시"
    timelist.append(t)
for tmp in district:
    districtlist.append(tmp.text)
for tmp in microdust:
    microdustlist.append(int(tmp.text))
for tmp in nanodust:
    nanodustlist.append(int(tmp.text))

dic = {}
dic['time'] = timelist
dic['district'] = districtlist
dic['microdust'] = microdustlist
dic['nanodust'] = nanodustlist

df = pd.DataFrame(dic)
#print(df)

print('서울 미세먼지 수치를 알고싶은 지역을 입력하세요 ex)OO구')
a = input()

tmp = df['district']==a
dist = df[tmp]

print(dist)