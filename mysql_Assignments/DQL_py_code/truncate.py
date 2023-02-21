import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

mycursor = mydb.cursor()

mycursor.execute("truncate table mysql_assignment.create")

mycursor.execute("select * from mysql_assignment.create")

for i in mycursor.fetchall():
    print(i)

mydb.close()