import curses
from unittest import result
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456@aya",database='aya')
mycursor=mydb.cursor()

'''sql=("INSERT INTO subject(name,degree)values(%s,%s)")
data=(["asmaa","30"],
["maher","40"],
["mo","90"],
["saleh","60"]
'''

'''for execute only one row of data
mycursor.execut(sql,data)'''
'''

for saving data to show
mydb.commit()'''
'''count rows in database
print(mycursor.rowcount)'''
'''show databases method'''
'''mycursor.execute("CREATE DATABASE aya")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)'''

'''to bring all data from database
mycursor.execute('select * from subject')
result=mycursor.fetchall()
for name in result:
    print(name)'''
'''
mycursor.execute('select name from subject')
result=mycursor.fetchone()
print(result)
'''
'''
mycursor.execute('select name from subject limit 5')
result=mycursor.fetchall()
print(result)
'''

mycursor.execute('select name from subject limit 5 of set 3')
result=mycursor.fetchall()
print(result)



