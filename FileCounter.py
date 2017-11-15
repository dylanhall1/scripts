'''
Useful tool if you want to see how many types of files are
in a folder. Output example:
p12: 1
rtf: 2
ini: 1
pdf: 1
txt: 2
jpg: 1
'''

import os, glob
from collections import Counter

directory = raw_input("Please Enter the Directory you wish to Scan:\nSuch as C:Users\username\documents\n")
# EXAMPLE "C:\Users\\username\Dropbox"
os.chdir(directory) # dont need this if you copy it somewhere
filelist = []
for file in glob.glob("*.*"):
    filelist.append( file[-3:].lower())

filecounter = dict(Counter(filelist))
for i in filecounter:
    print"{}: {}".format(i, filecounter.get(i))
