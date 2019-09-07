#!C:/Python27/python.exe
print "content-type:text/html\r\n\r\n"


import cgi,cgitb

form=cgi.FieldStorage()
a=form.getvalue('txt1')
b=form.getvalue('txt2')
print a
print b

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","event_planner")
cursor=db.cursor()


sel="select * from registration where email='%s'"%a
cursor.execute(sel)

data=cursor.fetchone()

if data[2]==a:
  print"<script>window.location.href='profile.py?id=%s';alert('login success');</script>"%(data[0])
else:
  print "login failed"
  
  
  
  
  