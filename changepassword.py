#!C:/python27/python.exe
print "content-type:text/html\r\n\r\n"
import cgi,cgitb
form=cgi.FieldStorage()
a=form.getvalue("id")

print"""
<html>
<head>
 <head>
<body>
<h1>user Change Password</h1>
<form action="changepasscode.py" method="post">
<input type="hidden" name="id" value="%s"/>"""%(a)
print"""
<br/>
Old Password<input type="text" name="opass"/><br/><br/>
New Password<input type="text" name="npass"/><br/><br/>
Confirm Password<input type="text" name="cpass"/><br/><br/>
<button type="submit">Change</button>
</body>
</html>
"""