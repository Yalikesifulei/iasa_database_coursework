from flask import Flask, render_template, abort, request
import pymysql
from db_connect import db
from queries import queries


tables = {'chairs': 'Кафедри', 'faculties': 'Факультети', 'groups': 'Групи', 
          'session': 'Сесія','students': 'Студенти', 'subjects': 'Дисципліни', 
          'teachers': 'Викладачі', 'teachers_subjects': 'Викладачі та предмети'}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tables=tables)

@app.route('/tables/<string:table_name>')
def select_table(table_name):
    if table_name not in tables:
        abort(404)
    with db.cursor() as cursor:
        cursor.execute(f'select * from `{table_name}`')
        columns = [desc[0] for desc in cursor.description]
        records = cursor.fetchall()
    return render_template('table.html', table_name=tables[table_name], table=records, columns=columns)

@app.route('/queries/<string:task>', methods=['GET', 'POST'])
def query(task):
    if task not in queries:
        abort(404)
    return_res = False
    if request.method == 'POST':
        form_data = [request.form.get(field.real_name) or -1 for field in queries[task]]
        with db.cursor() as cursor:
            q = f"call {task}("
            for field, data in zip(queries[task], form_data):
                q += f"@{field.real_name} := '{data}', "
            q = q[:-2] + ')'
            print(q)
            cursor.execute(q)
            columns = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
        return_res = True
    if request.method == 'GET':
        records, columns, form_data = [], [], []     
    return render_template('queries.html', task=task, fields=queries[task], 
                            table=records, columns=columns, return_res=return_res, form_data=form_data)

if __name__ == "__main__":
    app.run()