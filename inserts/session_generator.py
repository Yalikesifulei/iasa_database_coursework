import pymysql
import pandas as pd
import random

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='galganov',
    database='kursach'
)

with db.cursor() as cursor:
    cursor.execute(f'''select t1.`student_id`, t2.`subject_id`, t2.`teacher_id` from `students` t1 
        join `schedule` t2 on t1.group_code = t2.group_code
        join `subjects` t3 on t2.subject_id = t3.subject_id
        where t2.lesson_type = 'lec' and t3.subject_control = 'екзамен'; ''')
    lec = list(cursor.fetchall())
    cursor.execute(f'''select t1.`student_id`, t2.`subject_id`, t2.`teacher_id` from `students` t1 
        join `schedule` t2 on t1.group_code = t2.group_code
        join `subjects` t3 on t2.subject_id = t3.subject_id
        where (t2.lesson_type = 'prac' or t2.lesson_type = 'lab') and t3.subject_control = 'залік'; ''')
    prac = list(cursor.fetchall())
    cursor.execute(f'''select t1.`student_id`, t2.`subject_id`, t2.`teacher_id` from `students` t1 
        join `schedule` t2 on t1.group_code = t2.group_code
        join `subjects` t3 on t2.subject_id = t3.subject_id
        where t2.lesson_type = 'cw'; ''')
    cw = list(cursor.fetchall())
    cursor.execute(f'''select `student_id`, `scholarship` from `students`''')
    students = list(cursor.fetchall())

session_data = lec + prac + cw
students = pd.DataFrame(students, columns=['student_id', 'scholarship'])
students = students.set_index('student_id')
students = students.squeeze()
session_data = pd.DataFrame(session_data, columns=['student_id', 'subject_id', 'teacher_id'])
student_ids = session_data['student_id'].to_numpy()

random.seed(42)
marks = []
for student_id in student_ids:
    if students[student_id] == 1892:
        marks.append(random.randint(86, 100))
    elif students[student_id] == 1300:
        marks.append(random.randint(76, 100))
    elif students[student_id] == 0:
        marks.append(random.randint(60, 100))

session_data['mark'] = marks
session_data.to_csv('./inserts/session.csv', index=False)