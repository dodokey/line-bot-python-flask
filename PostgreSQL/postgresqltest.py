import psycopg2
import random

try:
    from apiTest.envvarrr import *
except:
    try:
        from envvarrr import *
# 連線至存在的資料庫
conn = psycopg2.connect(
    database=dbKeydatabase,
    user=dbKeyuser,
    password=dbKeypassword,
    host=dbKeyhost,
    port=dbKeyport)

cur = conn.cursor()

# cur.execute(
#     "INSERT INTO rfaapic (picurl) VALUES ('https://i.imgur.com/HIEzpKO.jpg');")

# clear table data
# cur.execute("TRUNCATE TABLE userOrGroupID;")
# conn.commit()

# z = '1aaaa哈哈aaaa哈zzzz'
# cur.execute("INSERT INTO contentlog (content) VALUES ('" + z + "');")

# cur.execute(
#     "INSERT INTO userOrGroupID (type, name, id) VALUES (1, '天天 mom', 'C01b8aa4a3bf365910708be6a8e6f1842');")
cur.execute("SELECT * FROM userOrGroupID;")
# thispic = random.randint(0, cur.rowcount - 1)
# print(thispic)
# print(cur.fetchall())

# fetchall() #一次取全部
# fetchone() #一次取一筆

row = cur.fetchone()
while row is not None:
    print(row[2])
    # print(type(row))
    row = cur.fetchone()

conn.commit()

# 關閉  PostgreSQL 資料庫連線
conn.close()

# ============================================tmp============================================
# cur.execute("INSERT INTO test (id, num, data) VALUES ('4', 123, '1aaaa哈哈哈');")
# cur.execute("CREATE TABLE contentlog (content varchar);")
# cur.execute("CREATE TABLE rfaapic (picurl varchar);")

# cur.execute("CREATE TABLE userOrGroupID (type integer, name varchar, id varchar);")
# userOrGroupID[type]: 0 user, 1 group
