#!C:/Python27/python.exe
print "content-type:text/html\r\n\r\n"


import cgi,cgitb

form=cgi.FieldStorage()
a=form.getvalue("name")
b=form.getvalue("email")
d=form.getvalue("subject")
e=form.getvalue("message")
print e

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","event_planner")
cursor=db.cursor()
ins="insert into contact(name,email,subject,message)values('%s','%s','%s','%s')"%(a,b,d,e)

cursor.execute(ins)
db.commit()
print "<script>window.location.href='contact.py';alert('contact data saved');</script>"