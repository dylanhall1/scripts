'''
This script reads in a list of names from the first column
in a spreadsheet, the renames all of the pdfs in that based
off the PDF naming
PDF0001
PDF0002
PDF0003
etc
Author: Dylan Hall
'''
import csv,glob,os,sys  #basic imports

def sort_keys(s):
    #defining the split method to rename the files
    s,n = s.split('split_')
    return s, int(n)

#Change TEST NAMES .csv to the csv of your choice
with open('Test Names.csv', 'r') as f: #File open
    pdfs = glob.glob('*.pdf')
    reader = list(csv.reader(f))
    if len(pdfs)!=len(reader): #matches number of files and numbers in spreadsheet column
       raise Exception("Length mismatch")

    pdflist = []
    for pdfname in pdfs:
        #this removes the ".pdf so I can sort by the end number"
        pdflist.append(pdfname[:-4])

    pdflist.sort(key=sort_keys)

    for something,row in zip(pdflist,reader): #running two 'for' statements together with zip
        os.rename(something+".pdf",row[0]+".pdf")
