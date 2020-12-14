from mysql import connector

from get_IDList import IDParser

from get_Info_From_ID import getInfo
from get_Size_From_ID import getSize

from multiprocessing import Pool
import time

def inputInfo(pantsDic):
    try:
        print(pantsDic)

        conn = connector.connect(**config)

        cursor = conn.cursor()

        sql = """
            INSERT INTO pants (id, name, category, popular, sales, img, price, sex)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (int(pantsDic["id"]), pantsDic["name"], pantsDic["category"], float(pantsDic["popular"]), int(pantsDic["sales"]), pantsDic["img"], int(pantsDic["price"]), pantsDic["sex"])

        cursor.execute(sql, data)

        conn.commit()
        conn.close()

    except connector.Error as err:
        print(err)


def inputSize(sizeDic):
    if sizeDic is not None:
        try:
            print(sizeDic)

            conn = connector.connect(**config)

            cursor = conn.cursor()

            for size in sizeDic:
                sql = """
                    INSERT INTO pants_size (id, num, length, waist, thigh, rise, hem)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

                data = (int(size["id"]), int(size["num"]), float(size["length"]), float(size["waist"]),float(size["thigh"]),float(size["rise"]),float(size["hem"]))

                cursor.execute(sql, data)

                conn.commit()

            conn.close()

        except connector.Error as err:
            print(err)


config = {
    "user" : "root",
    "password" : "gh175366",
    "host":"127.0.0.1",
    "database" : "fitest",
    "port":"3306"
}


if __name__ == '__main__':    
    # 아이디 리스트 가져오기
    pageList = IDParser()
    pool = Pool(processes=8)

    pagenum = 1
    for page in pageList:
        print("page : ",pagenum)
        resultDic = pool.map(getInfo, page)

        pool.map(inputInfo, resultDic)
        
        pagenum = pagenum+1

    pagenum = 1
    for page in pageList:
        print("page : ", pagenum)
        
        resultDic = pool.map(getSize,page)

        pool.map(inputSize, resultDic)

        pagenum = pagenum+1
