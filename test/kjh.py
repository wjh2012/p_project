from urllib.request import urlopen
from bs4 import BeautifulSoup

def parsing(url, id):
    bsObject = BeautifulSoup(url, "html.parser") 

    size_category_list = []
    size_tbody_list = []
    item_category_list = []
    # 아이템의 카테고리 확인( ex)상의, 맨투맨/스웨트셔츠', )
    item_category = bsObject.select(
        '#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > div.product_info > p > a'
    )
    # 사이즈의 테이블을 전부 확인
    size_table = bsObject.select(
        '#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > div.wrap_product > div.product_left > div.box_material > table'
    )
    # 사이즈 테이블의 카테고리 확인
    size_category = bsObject.select(
        '#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > div.wrap_product > div.product_left > div.box_material > table > thead > tr > th'
    )
    # 사이즈의 상세지표 확인
    size_tbody = bsObject.select(
        '#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > div.wrap_product > div.product_left > div:nth-child(4) > table > tbody > tr'
    )

    for title in item_category: # 상품의 카테고리를 확인함.
        ## Tag안의 텍스트
        item_category_list.append(title.text)
    if len(item_category_list) == 0:
        return
    #try:
    #    if item_category_list[0] != "바지":
    #        return
    #except:
    #    return  


    for tmp in size_category: # 사이즈 테이블에서 카테고리를 확인한다.
        size_category_list.append(tmp.text.strip()) 

    for tmp in size_tbody:
        size_tbody_list.append(tmp.text)

    ### 사이즈 전처리 과정(문자열 제거, 공백을 리스트로 나누기)
    if len(size_tbody_list) > 2:
        del size_tbody_list[0], size_tbody_list[0] # n가지고 계신 제품의....., 구매내역의 사이즈.... 문자열제거

    size_list = []
    for size_line in size_tbody_list:
        tmp = size_line.split("\n")
        del tmp[0]
        tmp.pop()
        size_list.append(tmp)

    print("id : " + str(id)) 
    print(item_category_list)
    print(size_category_list)
    print(size_list)

if __name__ == "__main__":
    for i in range(1444444, 2000000):
        html = urlopen("https://store.musinsa.com/app/product/detail/"+str(i)+"/0")  
        parsing(html, i)
