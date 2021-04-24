from flask import Flask, render_template, abort
import pymysql
from db_connect import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

tables = ['chairs', 'faculties', 'groups', 'session', 
          'students', 'subjects', 'teachers', 'teachers_subjects']

@app.route('/tables/<string:table_name>')
def select_table(table_name):
    if table_name not in tables:
        abort(404)
    with db.cursor() as cursor:
        cursor.execute(f'select * from `{table_name}`')
        columns = [desc[0] for desc in cursor.description]
        records = cursor.fetchall()
    return render_template('table.html', table=records, columns=columns)

if __name__ == "__main__":
    app.run()