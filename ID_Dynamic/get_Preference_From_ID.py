from selenium import webdriver

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

def getPreference(pantsID):
    driver.get("https://store.musinsa.com/app/goods/"+str(pantsID))
    result = driver.find_elements_by_class_name('bar_num')

    preference = []

    for prefer in result:
        if prefer.text:
            preference.append(prefer.text.split("%")[0])
        
    print(pantsID)
    print(preference)

getPreference(1357807)

driver.quit()
