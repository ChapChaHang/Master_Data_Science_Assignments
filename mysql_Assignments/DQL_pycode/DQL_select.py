import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

mycursor = mydb.cursor()
mycursor.execute("create table if not exists mysql_assignment.marks(name varchar(10),age int(3),marks varchar(3))")
mycursor.execute('INSERT INTO mysql_assignment.marks VALUES("sham",19,"B");')
mycursor.execute('INSERT INTO mysql_assignment.marks VALUES("ram",29,"A");')
mycursor.execute('INSERT INTO mysql_assignment.marks VALUES("bam",39,"C");')


mycursor.execute('select * from mysql_assignment.marks')
for i in mycursor.fetchall():
    print(i)
mydb.close()