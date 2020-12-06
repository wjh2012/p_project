from mysql import connector

from get_IDList import IDParser

from get_Info_From_ID import getInfo
from get_Size_From_ID import getSize

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
    try:
        print(sizeDic)

        conn = connector.connect(**config)

        cursor = conn.cursor()

        sql = """
            INSERT INTO pants_size (id, num, length, waist, thigh, rise, hem)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        data = (int(sizeDic["id"]), int(sizeDic["num"]), float(sizeDic["length"]), float(sizeDic["waist"]),float(sizeDic["thigh"]),float(sizeDic["rise"]),float(sizeDic["hem"]))

        cursor.execute(sql, data)

        conn.commit()
        conn.close()

    except connector.Error as err:
        print(err)


config = {
    "user" : "root",
    "password" : "gh175366",
    "host":"127.0.0.1",
    "database" : "fit",
    "port":"3306"
}

# 아이디 리스트 가져오기
IDList = IDParser()

pagenum = 1

for page in IDList:
    print("page : ",pagenum)
    
    for pantsID in page:
        inputInfo(getInfo(pantsID))
    pagenum = pagenum+1

pagenum = 1
for page in IDList:
    print("page : ",pagenum)
    for pantsID in page:
        if getSize(pantsID) is not None:
            for size in getSize(pantsID):
                inputSize(size)
    pagenum = pagenum+1
