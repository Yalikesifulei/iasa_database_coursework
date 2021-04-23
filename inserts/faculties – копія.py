import pymysql

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='galganov',
    database='kursach_v1'
)

subjects = ['Інститут прикладного функціонального аналiзу',
             'Факультет інженерно-обчислювальних технологій',
             'Холодноенергетичний факультет']

cursor = db.cursor()
for ind, fac in enumerate(subjects):
    request = f"insert into subjects (faculty_id, faculty_name, headmaster_id) values ({ind}, '{fac}', 0)"
    cursor.execute(request)
    db.commit()

request = "select * from subjects"
cursor.execute(request)
results = cursor.fetchall()
print(results)