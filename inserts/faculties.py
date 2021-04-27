import pymysql

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='galganov',
    database='kursach_v1'
)

faculties = ['Інститут прикладного функціонального аналiзу',
             'Факультет гуманітарних наук',
             'Холодноенергетичний факультет']

cursor = db.cursor()
for ind, fac in enumerate(faculties):
    request = f"insert into faculties (faculty_id, faculty_name, headmaster_id) values ({ind}, '{fac}', 0)"
    cursor.execute(request)
    db.commit()

request = "select * from faculties"
cursor.execute(request)
results = cursor.fetchall()
print(results)