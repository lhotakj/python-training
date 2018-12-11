import sqlite3
conn=sqlite3.connect("pokus.sqlite")
cursor=conn.cursor()
cursor.execute("select * from phone_numbers")
for record in cursor.fetchall():
  print("Name : %s, phone number : %s" %(record[0],record[1]))
conn.close()
