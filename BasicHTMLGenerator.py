'''
Basic HTML5 doctype for quick use if you just need to output a file
Helps if you have people ask you how to do inline CSS
'''

from sys import argv
script,filename = argv
contents = '''
<!DOCTYPE html>
<html>
<head>
<title> New HTML page </title>
</head>
<body>
<p> Hello world! </p>
</body>
</html>
'''
print "Opening File:"
target = open(filename + '.html','w')
print "Writing File:"
target.write(contents)
print "Closing File:"
target.close()
