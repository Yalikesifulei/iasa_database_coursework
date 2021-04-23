from flask import Flask, render_template
import pymysql
from db_connect import db

app = Flask(__name__)

tname = 'subjects'
@app.route('/')
def main():
    cursor = db.cursor()
    sql = f"select * from {tname}"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template(f'{tname}.html', results=results)

if __name__ == "__main__":
    app.run()