#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("Content-type: text/js")
print()

form=cgi.FieldStorage()
no=form.getvalue("que_numb")
nm=form.getvalue("que_text")
aw=form.getvalue("optionSelected(this)")

con=mysql.connector.connect(host="localhost",user="root",password="Bhushan@123",database="exam")
curs=con.cursor()

curs.execute("insert into test values(%s,%s,%s);"%(no,nm,aw))
rec=curs.fetchone()
if rec:
    
    print("data instered ")
else:
    print("data not insetred ")
    con.close()


