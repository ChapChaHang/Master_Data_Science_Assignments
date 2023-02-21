import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

mycursor = mydb.cursor()
mycursor.execute('update mysql_assignment.marks set marks="a" where name="bam"')
mycursor.execute('select * from mysql_assignment.marks')
for i in mycursor.fetchall():
    print(i)
mydb.close()