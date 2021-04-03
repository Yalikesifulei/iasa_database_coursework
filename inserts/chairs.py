import pymysql

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='galganov',
    database='kursach_v1'
)

chairs = ['Чисельних методів функціонального аналізу', 'Квазілінійного проектування']

cursor = db.cursor()
for ind, chair in enumerate(chairs):
    request = f"insert into chairs (chair_id, faculty_id, chair_name) values (0{ind}, 0, '{chair}')"
    cursor.execute(request)
    db.commit()

chairs = ['Наближених обчислень']

cursor = db.cursor()
for ind, chair in enumerate(chairs):
    request = f"insert into chairs (chair_id, faculty_id, chair_name) values (1{ind}, 1, '{chair}')"
    cursor.execute(request)
    db.commit()

chairs = ['Наднизьких температур', 'Надвисоких енергій']

cursor = db.cursor()
for ind, chair in enumerate(chairs):
    request = f"insert into chairs (chair_id, faculty_id, chair_name) values (2{ind}, 2, '{chair}')"
    cursor.execute(request)
    db.commit()

request = "select * from chairs"
cursor.execute(request)
results = cursor.fetchall()
print(results)