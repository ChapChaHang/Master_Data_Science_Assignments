import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE if not exists mysql_assignment")
    mycursor.execute("CREATE TABLE if not exists mysql_assignment.create(name VARCHAR(15),phoneno INT(10),state VARCHAR(15),city VARCHAR(15))")
except Exception as e:
    print("Error ==> {}".format(e))
finally:    
    mydb.close()