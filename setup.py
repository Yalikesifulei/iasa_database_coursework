import pymysql
import sys
import getpass
import time

def update_config(host, port, user, password):
    with open('db_connect.py', 'w') as f:
        f.writelines(["import pymysql\n\n",
                      "db = pymysql.connect(\n",
                      f"\thost='{host}',\n",
                      f"\tport={port},\n",
                      f"\tuser='{user}',\n",
                      f"\tpassword='{password}',\n",
                      f"\tdatabase='univ_db'\n)"])

# https://stackoverflow.com/questions/745538/create-function-through-mysqldb
def execute_script(fname, db):
    delimiter = ';'
    statement = ""
    with open(fname, encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('delimiter'):
                delimiter = line[10:]
            else:
                statement += line + '\n'
                if line.endswith(delimiter):
                    statement = statement.strip().strip(delimiter)
                    with db.cursor() as cursor:
                        try:
                            cursor.execute(statement)
                            db.commit()
                            statement = ""
                        except cursor.Error as e:
                            print(f"{fname} - error applying ({str(e)})\nstatement:{statement}\nterminating...")
                            sys.exit(1)

if __name__ == '__main__':
    print('enter connection parameters:')
    host = input('\thost (leave empty for default localhost): ') or 'localhost'
    port = input('\tport (leave empty for default 3307): ') or 3307
    user = input('\tuser (leave empty for default root): ') or 'root'
    password = getpass.getpass(f'\tpassword for {user}: ')
    update_config(host, port, user, password)
    db = pymysql.connect(host=host, port=port, user=user, password=password)
    print('creating schema and tables...')
    tock = time.time()
    execute_script('./inserts/create_tables.sql', db)
    tick = time.time()
    print(f'\tdone in {(tick-tock):.3f} sec')
    db = pymysql.connect(host=host, port=port, user=user, password=password, database='univ_db')
    print('inserting data...')
    tock = time.time()
    execute_script('./inserts/faculties.sql', db)
    execute_script('./inserts/chairs.sql', db)
    execute_script('./inserts/teachers.sql', db)
    execute_script('./inserts/groups.sql', db)
    execute_script('./inserts/students.sql', db)
    execute_script('./inserts/subjects.sql', db)
    execute_script('./inserts/schedule.sql', db)
    execute_script('./inserts/mega_session.sql', db)
    tick = time.time()
    print(f'\tdone in {(tick-tock):.3f} sec')
    print('creating stored procedures...')
    tock = time.time()
    for i in range(1, 14):
        execute_script(f'./queries/task_{i}.sql', db)
    tick = time.time()
    print(f'\tdone in {(tick-tock):.3f} sec')
    print('database is ready!')