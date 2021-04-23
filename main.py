from flask import Flask, render_template
import pymysql
from db_connect import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

tname = 'subjects'
@app.route('/chairs')
def chairs():
    cursor = db.cursor()
    sql = f"select * from `chairs`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('chairs.html', results=results)

@app.route('/faculties')
def faculties():
    cursor = db.cursor()
    sql = f"select * from `faculties`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('faculties.html', results=results)

@app.route('/groups')
def groups():
    cursor = db.cursor()
    sql = f"select * from `groups`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('groups.html', results=results)

@app.route('/session')
def session():
    cursor = db.cursor()
    sql = f"select * from `session`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('session.html', results=results)

@app.route('/students')
def students():
    cursor = db.cursor()
    sql = f"select * from `students`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('students.html', results=results)

@app.route('/subjects')
def subjects():
    cursor = db.cursor()
    sql = f"select * from `subjects`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('subjects.html', results=results)

@app.route('/teachers')
def teachers():
    cursor = db.cursor()
    sql = f"select * from `teachers`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('teachers.html', results=results)

@app.route('/teachers_subjects')
def teachers_subjects():
    cursor = db.cursor()
    sql = f"select * from `teachers_subjects`;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('teachers_subjects.html', results=results)

if __name__ == "__main__":
    app.run()