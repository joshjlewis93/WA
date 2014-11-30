#!/usr/bin/python
import cgi, cgitb
form = cgi.FieldStorage()
def Easter(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    return [p, n, y]

def supscript(p):
	return ("th" if 4<=p%100<=20 else {1:"st",2:"nd",3:"rd"}.get(p%10, "th"))
user_year = int(form.getvalue('theYear'))
day = Easter(user_year)[0]
supday = supscript(day)
month = Easter(user_year)[1]
months = ['March', 'April']
month_number = "0" + str(month)
month_text = months[month-3]
year = Easter(user_year)[2]

print ("Content-Type: text/html; charset=utf-8")
print ("")
print ("<!DOCTYPE html >")
print ("<html lang=”en”>")
print ("<head>")
print ("<title>Easter Day</title>")
print ("<meta charset=”utf-8” />")
print ("<link rel="stylesheet" type="text/css" href="css/Easter.css">")
print ("</head>")
print ("<body>")
print ("<header>")
print ("<h1>Find what day Easter will be!</h1>")
print ("</header>")
print ("<div id="wrapper">")
print ("<form id="form" method="POST" action="cgi-bin/Easter.py">")
print ("<label for="theYear">Enter a year and return format:</label>")
print ("<input type="text" id="theYear" name="theYear" /> <br />")
print ("<input type="radio" name="outputType" id="ddmmyy" value ="ddmmyy" checked="checked"> DD/MM/YYYY <br>")
print ("<input type="radio" name="outputType" id="dd_month_yyyy" value ="dd_month_yyyy"> Day Month Year <br>")
print ("<input type="radio" name="outputType" id="Both" value ="Both"> Both <br>")
print ("<input type="submit" value="submit" />")
print ("</form>")
print ("<div id="content">")
print("<p> You chose the year: </p>")
print("<br>")
print ("<p>"+ user_year + "</p>")
print ("<p>Easter falls on:</p>")
if form.getValue("outputType") == "ddmmyy":
	print("<p>" + day + "/" + month_number + "/" + year + "</p>"
elif form.getValue("outputType") == "dd_month_yyyy":
	print("<p>" + day + "<sup>" + supday + "</sup>" + " " + month_text + " " + year + "</p>"
elif form.getValue("outputType") == "Both":
	print("<p>" + day + "/" + month_number + "/" + year + "</p>"
	print("<br>")
	print("<p> or </p>")
	print("<br>")
	print("<p>" + day + "<sup>" + supday + "</sup>" + " " + month_text + " " + year + "</p>"
print ("</div>")
print ("</div>")       
print ("</body>")
print ("</html>")