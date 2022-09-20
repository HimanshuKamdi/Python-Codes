import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="himanshu",passwd="password")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
#creating required tables 
#mycursor.execute("create table if not exists bank_data(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
#mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
if mydb.is_connected:
    print("yesss")

    
    
