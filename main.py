from flask import Flask, render_template, abort, request
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

@app.route('/queries/task_1', methods=['GET', 'POST'])
def query_test():
    return_res = False
    if request.method == 'POST':
        group_code = request.form.get('group_code')
        study_year = request.form.get('study_year') or -1
        faculty_id = request.form.get('faculty_id') or -1
        sex = request.form.get('sex')
        age = request.form.get('age') or -1
        has_children = request.form.get('has_children') or -1
        scholarship = request.form.get('scholarship') or -1
        with db.cursor() as cursor:
            q = f'''call task_1(
                        @group_code := '{group_code}',
                        @study_year := {study_year},
                        @faculty_id := {faculty_id},
                        @sex := '{sex}',
                        @age := {age},
                        @has_children := {has_children},
                        @scholarship := {scholarship}
                    )'''
            q = ' '.join(q.split())
            print(q)
            cursor.execute(q)
            columns = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
        return_res = True
    
    if request.method == 'GET':
        records, columns = [], []
            
    return render_template('queries.html', table=records, columns=columns, return_res=return_res)

if __name__ == "__main__":
    app.run()