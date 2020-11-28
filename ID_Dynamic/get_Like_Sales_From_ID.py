from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from get_IDList import IDParser

path = "C:/Users/wjh20/Desktop/project/p_project/chromedriver_win32/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument('headless') 
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(path, options=options)

def getLikeSales(pantsID):
    driver.get("https://store.musinsa.com/app/goods/"+str(pantsID))

    LikeSales = []

    # 좋아요가 늦게 로딩됨, 로딩될때까지 대기
    #WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('prd_like_cnt')) 
    
    # 누적 판매량
    salesRaw = driver.find_element_by_id('sales_1y_qty')  
    salesFirst = salesRaw.text.split("개")[0]
    if '천' in salesFirst:
        sales = int(float(salesFirst.split('천')[0])*1000)
    elif '만' in salesFirst:
        sales = int(float(salesFirst.split('만')[0])*10000)
    else:
        sales = salesFirst    

    # 좋아요
    likeRaw = driver.find_element_by_class_name('prd_like_cnt')
    like = likeRaw.text.replace(',','')
    
    # 리스트에 좋아요, 누적판매 순으로 저장
    LikeSales.append(like)    
    LikeSales.append(sales)
        
    print(pantsID)
    print(LikeSales)

getLikeSales(979883)

driver.quit()
