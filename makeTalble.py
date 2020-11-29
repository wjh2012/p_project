from mysql import connector

config = {
    "user" : "root",
    "password" : "gh175366",
    "host":"127.0.0.1",
    "database" : "fit",
    "port":"3306"
}

try:
    conn = connector.connect(**config)

    cursor = conn.cursor()

    pantsSql ='''
        CREATE TABLE pants(
            id int,
            name nvarchar(50),
            category nvarchar(30),
            img nvarchar(200),
            price int,
            satisfaction float,
            review int            
            sex nvarchar(1),
            like

            PRIMARY KEY(id)
        );
    '''          
    cursor.execute(pantsSql)

    pants_sizeSql = '''
        CREATE TABLE pants_size(
            id int,
            length float,
            waist float,
            thigh float,
            rise float,
            hem float,
            FOREIGN KEY(id) REFERENCES pants(id) on delete cascade
        );
    '''
    cursor.execute(pants_sizeSql)

    conn.commit()
    conn.close()

except connector.Error as err:
    print(err)