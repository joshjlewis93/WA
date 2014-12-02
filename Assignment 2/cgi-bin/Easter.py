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

print ("Content-type: text/html")
print ("""
<html lang=”en”>
  <head>
    <title>Easter Day</title>
    <meta charset=”utf-8” />
    <link rel="stylesheet" type="text/css" href="css/easter.css">
  </head>
    <body>
    <header>
    <h1>Find what day Easter will be!</h1>
    </header>
    <div id="wrapper">
      <form id="form" action="cgi-bin/easter.py">
        <label for="theYear">Enter a year and return format:</label>
        <input type="text" id="theYear" name="theYear" /> <br />
        <input type="radio" name="outputType" id="ddmmyy" value ="ddmmyy" checked="checked"> DD/MM/YYYY <br>
        <input type="radio" name="outputType" id="dd_month_yyyy" value ="dd_month_yyyy"> Day Month Year <br>
        <input type="radio" name="outputType" id="Both" value ="Both"> Both <br>
        <input type="submit" value="submit" />
      </form>
""")
if form.getValue("outputType") == "ddmmyy":
    print ("<div id="content">")
    print ("<p> You chose the year: <br>")
    print (user_year + "<br>")
    print ("Easter falls on: <br>")
    print (day + "/" + month_number + "/" + year + "</p>")
    print ("""
    </div>
    </div>    
    </body>
</html>)
"""
if form.getValue("outputType") == "dd_month_yyyy":
    print ("<div id="content">")
    print ("<p> You chose the year: <br>")
    print (user_year + "<br>")
    print ("Easter falls on: <br>")
    print (day + supday + " " + month_text + " " + year + "</p>")
    print ("""
    </div>
    </div>    
    </body>
</html>)
"""
if form.getValue("outputType") == "Both":
    print ("<div id="content">")
    print ("<p> You chose the year: <br>")
    print (user_year + "<br>")
    print ("Easter falls on: <br>")
    print (day + supday + " " + month_text + " " + year + "<br>")
    print ("OR: <br>")
    print (day + supday + " " + month_text + " " + year + "</p>")
    print ("""
    </div>
    </div>    
    </body>
</html>)
"""