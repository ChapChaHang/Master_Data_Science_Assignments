import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

mycursor = mydb.cursor()
mycursor.execute('drop table mysql_assignment.create')

mydb.close()