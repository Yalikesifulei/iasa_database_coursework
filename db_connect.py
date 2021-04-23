import pymysql

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='galganov',
    database='kursach_v1'
)