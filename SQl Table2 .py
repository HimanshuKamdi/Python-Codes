import mysql.connector
#mycon=mysql.connector.connect(host='localhost',user='root',password='12345678')
mydb=mysql.connector.connect(host="localhost",user="himanshu",passwd="password")
cursor=mydb.cursor()
cursor.execute("create database if not exists school")
cursor.execute("use school")
cursor.execute("create table  if not exists student ( rollno int primary key, name varchar(29) not null, age int , class  varchar(9), city varchar (20))")
cursor.execute("Insert into student values (1,'Akash', 19, '12sci', 'Pune')")
cursor.execute("select * from student where rollno= 1")
details=cursor.fetchall()
print(details)
mydb.commit()
cursor.close





