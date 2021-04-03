from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='galganov',
    database='kursach_v1'
)

@app.route('/')
def main():
    cursor = db.cursor()
    sql = "select * from faculties"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run()