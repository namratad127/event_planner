#!C:/python27/python.exe
print "content-type:text/html\r\n\r\n"
import cgi,cgitb
form=cgi.FieldStorage()
a=form.getvalue("id")
b=form.getvalue("npass")
c=form.getvalue("cpass")
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","event_planner")
cursor=db.cursor()
up="update registration set password='%s' where id=%s"%(b,a)
res=cursor.execute(up)
print "<script>window.location.href='login.py';alert('password Change SuccessFully');</script>"
