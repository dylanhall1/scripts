'''
Using the cx_Oracle module for connections to our oracle database
Potential use in extracting data into a CSV file in a quick fashion
Maybe use HTML Generator to include this in or an XML file
'''

import cx_Oracle
connection = cx_Oracle.connect('USERNAME','PASSWORD','HOSTNAME:PORTNUMBER/SERVICEID')
cur = connection.cursor()
cur.execute('''SELECT *
             FROM TABLE''')

for row in cur:
    print row
cur.close()
con.close()
