import cx_Oracle
conn = cx_Oracle.connect("student/student@10.2.20.230:1521/orcl")
cursor = conn.cursor()
cursor.execute("select * from phone_numbers")
for record in cursor.fetchall():
    print("Name : %s, phone number : %s" % (record[0], record[1]))
conn.close()
