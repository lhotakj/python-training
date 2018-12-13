import os

import cx_Oracle

print(os.environ['PATH'])

conn = cx_Oracle.connect("student/student@10.2.20.230:1521/orcl")
cursor = conn.cursor()
cursor.execute("select * from phone_numbers")
