#!C:/Python27/python.exe
print "content-type:text/html\r\n\r\n"

import cgi,cgitb

form=cgi.FieldStorage()
a=form.getvalue("id")



import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","event_planner")
cursor=db.cursor()


sel="select * from registration where id=%s"%(a)
cursor.execute(sel)
data=cursor.fetchone()
print"""
<html>

<head>

</head>
<body>
<h1>user profile</h1>
<a href="changepassword.py?id=%s">change password</a>
<a href="home.py">logout</a>
<table border="1">
<tr>
<th>ID</th>
<th>NAME</th>
<th>EMAIL</th>
<th>PASSWORD</th>
</tr>
<tr>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
</tr>
</table>
</body>
</html>"""%(data[0],data[0],data[1],data[2],data[3])
