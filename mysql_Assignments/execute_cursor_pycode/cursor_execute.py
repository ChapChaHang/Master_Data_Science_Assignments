import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

new_cursor = db.cursor()
new_cursor.execute('insert into mysql_assignment.marks values("test",25,"B")')
new_cursor.execute('select * from mysql_assignment.marks')

for record in new_cursor.fetchall():
    print(record)

db.close()