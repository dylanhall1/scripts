'''
Essentially this will query a first name, last name, or department, or all and return the retrieved values
from the webpage and display it in a nice format.

https://pscal.pstcc.edu/adphonebook/Default.aspx?First+Name=&Last+Name=&Department=
'''
from bs4 import BeautifulSoup
import urllib
import re

#user input
first = raw_input('Please enter a first name.\n>')
last = raw_input('Please enter a last name.\n>')
department = raw_input('Please enter a department.\n>')

#the easiest way I could think to query the webpage
f = urllib.urlopen("https://pscal.pstcc.edu/adphonebook/Default.aspx?First+Name="+first+
                   "&Last+Name="+last+"&Department="+department)

#this css style is only on the data we need, the regex is as the location has a different value after nowrap;
pageinfo = re.compile("vertical-align:Middle;white-space:nowrap;*")
soup = BeautifulSoup(f, 'html.parser')
info = soup.find_all("td",{"class":"dxgv", "style": pageinfo})
#easy display for now
for i in info:
    print i.string