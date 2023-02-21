import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

mycursor = mydb.cursor()
mycursor.execute("create table if not exists mysql_assignment.marks(name varchar(10),age int(3),marks varchar(3))")
mycursor.execute('insert into mysql_assignment.marks values("eam",20,"c")')
mycursor.execute('insert into mysql_assignment.marks values("ram",19,"b")')
mycursor.execute('insert into mysql_assignment.marks values("sam",22,"a")')


mycursor.execute('select * from mysql_assignment.marks')
for i in mycursor.fetchall():
    print(i)
mydb.close()