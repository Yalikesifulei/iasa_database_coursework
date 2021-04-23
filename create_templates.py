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
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    </head>
    <body>
        <table class="table table-striped">
            <thead class="thead-light">
            <tr>
"""

for table in tables:
    print(table[0])
    cursor.execute(f"describe `{table[0]}`;")
    columns = cursor.fetchall()
    with open(f'./templates/{table[0]}.html', 'w') as fout:
        fout.write(template)
        for col in columns:
            fout.write(f'\t\t\t\t<th scope="col">{col[0]}</th>\n')
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