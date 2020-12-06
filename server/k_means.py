import pymysql
import mysql.connector
from sklearn.cluster import KMeans
import numpy as np
import pickle


config = {
    "user": "root",
    "password": "gh175366",
    "host": "127.0.0.1", #local
    "database": "fit", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

def Select():
    try:
        conn = mysql.connector.connect(**config)
        print(conn)
        # db select, insert, update, delete 작업 객체
        cursor = conn.cursor()
        # 실행할 select 문 구성
        sql = "SELECT * FROM pants_size ORDER BY 1 DESC"
        # cursor 객체를 이용해서 수행한다.
        cursor.execute(sql)
        # select 된 결과 셋 얻어오기
        resultList = cursor.fetchall()  # tuple 이 들어있는 list
        
        size_list_dict=[]
        for result in resultList:
            tmp_dict ={}
            tmp_dict['id'] = result[0]  # seq
            tmp_dict['num'] = result[1]  # title
            tmp_dict['length'] = result[2]  # content
            tmp_dict['waist'] = result[3]  # content
            tmp_dict['thigh'] = result[4]  # content
            tmp_dict['rise'] = result[5]  # content
            tmp_dict['hem'] = result[6]  # content
            size_list_dict.append(tmp_dict)
        
        print(size_list_dict)
        return size_list_dict
    except mysql.connector.Error as err:
        print(err)

def Update(sum_list):
    try:
        for index, tmp in enumerate(sum_list):
            conn = mysql.connector.connect(**config)
            print(conn)
            # db select, insert, update, delete 작업 객체
            cursor = conn.cursor()
            # 실행할 select 문 구성
            sql = """update pants_size set model_group =%s where id=%s and num=%s"""
            tmp = (int(tmp[2]), int(tmp[0]), int(tmp[1]))
            # cursor 객체를 이용해서 수행한다.
            cursor.execute(sql,tmp)
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(err)

def dictListToList(list_dict):
    size_list=[]
    idnum_list=[]
    for tmp in list_dict:
        tmp_list = list(tmp.values())
        # 필요없는 id와 num제거
        idnum_list.append([tmp_list[0],tmp_list[1]])
        del tmp_list[0]
        del tmp_list[0]
        size_list.append(tmp_list)
    print(idnum_list)
    return size_list,idnum_list

def Learn(size_list):
    print("학습을 시작한다.")
    kmeans = KMeans(n_clusters=10, random_state=0).fit(size_list)
    group = kmeans.labels_
    pickle.dump(kmeans, open("save.pkl", "wb")) # 모델 저장
    return group

def sum_group_id(idnum_list, group):
    # id와 num, group을 합치는 작업진행
    for index,val in enumerate(idnum_list):
        val.append(group[index])
    return idnum_list

if __name__ == "__main__":
    size_list_dict = Select()
    size_list,idnum_list = dictListToList(size_list_dict)
    group = Learn(size_list)
    sum_list = sum_group_id(idnum_list, group)
    Update(sum_list)