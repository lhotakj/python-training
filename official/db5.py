import cx_Oracle
conn=cx_Oracle.connect("student/student@10.2.20.230:1521/orcl")
cursor=conn.cursor()
cursor1=conn.cursor()
radky=[('prvni','1'),('druhy','2'),('treti','3')]
typ_record=conn.gettype("PACK1.ZAZNAM")
typ_tab=conn.gettype("PACK1.KOLEKCE")
tab=typ_tab.newobject()
record=typ_record.newobject()
record.NAME='Praha'
record.PHONE='44444444'
tab.append(record)
record.NAME='Brno'
record.PHONE='55555555'
tab.append(record)
#new insert
cursor1.callproc("PACK1.VLOZ",[tab])
conn.commit()
cursor.execute("select * from phones")
for record in cursor.fetchall():
  print("Name : %s, phone number : %s" %(record[0],record[1]))
conn.close()
