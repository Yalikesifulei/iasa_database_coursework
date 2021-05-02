from flask import Flask, render_template, abort, request
import pymysql
from db_connect import db
from queries import queries


tables = {'chairs': 'Кафедри', 'faculties': 'Факультети', 'groups': 'Групи', 
          'session': 'Сесія','students': 'Студенти', 'subjects': 'Дисципліни', 
          'teachers': 'Викладачі', 'schedule': 'Розклад'}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', queries=queries)

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
        form_data = []
        for field in queries[task].fields:
            form_data.append(request.form.get(field.real_name))
            if not form_data[-1] and field.field_type == 'date':
                form_data[-1] = '0000-00-00'
            if not form_data[-1] and field.field_type != 'date':
                form_data[-1] = -1
        with db.cursor() as cursor:
            q = f"call {task}("
            for field, data in zip(queries[task].fields, form_data):
                q += f"@{field.real_name} := '{data}', "
            q = q[:-2] + ')'
            print(q)
            cursor.execute(q)
            columns = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
        return_res = True
    if request.method == 'GET':
        records, columns, form_data = [], [], []     
    return render_template('queries.html', task=task, descr=queries[task].description, fields=queries[task].fields, 
                            table=records, columns=columns, return_res=return_res, form_data=form_data)

if __name__ == "__main__":
    app.run()