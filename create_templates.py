import pymysql
from db_connect import db

cursor = db.cursor()

cursor.execute("show tables")
tables = cursor.fetchall()

template = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Untitled Document</title>
    </head>
    <body>
        <table>
            <thead>
            <tr>
"""

for table in tables:
    print(table[0])
    cursor.execute(f"select `COLUMN_NAME` from `INFORMATION_SCHEMA`.`COLUMNS`  where `TABLE_NAME` = '{table[0]}'")
    columns = cursor.fetchall()
    with open(f'./templates/{table[0]}.html', 'w') as fout:
        fout.write(template)
        for col in columns:
            fout.write(f'\t\t\t\t<th>{col[0]}</th>\n')
        fout.write("""
        </tr>
            </thead>
            <tbody>
                {%for row in results%}
                    <tr>\n""")
        for i in range(len(columns)):
            fout.write(f'\t\t\t\t\t\t<td>{{{{row[{i}]}}}}</td>\n')
        fout.write("""
                    </tr>
                {%endfor%}
            </tbody>
        </table>
    </body>
</html> """)