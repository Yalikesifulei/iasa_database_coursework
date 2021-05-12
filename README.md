# iasa_database_coursework
WebUI as a static website with Flask and a MySQL database as coursework for Database course
***
**Installation**: 
1. Make sure [MySQL server](https://dev.mysql.com/downloads/mysql/) ≥ 8.0 is installed and running, Python ≥ 3.9 and newest versions of [Flask](https://pypi.org/project/Flask/), [PyMySQL](https://pypi.org/project/PyMySQL/)
and [cryptography](https://pypi.org/project/cryptography/) are installed. 
2. Copy this repository and run `setup.py` to connect to SQL server, create database, procedures and insert
test data:
```
PS C:\Users\Yalikesi\...\iasa_database_coursework> python setup.py
enter connection parameters:
        host (leave empty for default localhost):
        port (leave empty for default 3307):
        user (leave empty for default root):
        password for root:
creating schema and tables...
        done in 0.997 sec
inserting data...
        done in 0.766 sec
creating stored procedures...
        done in 0.219 sec
database is ready!
```
3. Now you can run `main.py` to use WebUI at `127.0.0.1:5000`.
