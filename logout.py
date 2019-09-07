#!C:/python27/python.exe
print "content-type:text/html\r\n\r\n"
import cgi,cgitb
form=cgi.FieldStorage()
a=form.getvalue("id")
print a
if a:
  print "<script>window.location.href='login.py';alert('logout success');</script>"