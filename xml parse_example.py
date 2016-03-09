import os, glob, re
from xml.dom import minidom
import sys

#path = ('C:/nltk_data/tutorial/*.xml')
#TOTALXML = len(glob.glob(os.path.join(path, '*.xml')))
#print(TOTALXML)

for xmlfile in glob.glob('C:/nltk_data/english/*.xml') :
    #print(xmlfile)
    xmldoc = minidom.parse(xmlfile)

    author = xmldoc.getElementsByTagName("author")[0]

    documents = author.getElementsByTagName("document")

    with open('C:/nltk_data/english/output/output.txt', 'a') as f:  
        for document in documents:
            firstchild = document.firstChild.data
       #     sys.stdout = f
            print(firstchild)
            f.write(firstchild)
      # sys.stdout = open("output.txt", 'w')    
    

    
# Check current working directory.
#retval = os.getcwd()
#print("Current working directory %s" % retval)

#os.chdir(path)


#xmldoc = minidom.parse('*.xml')

#author = xmldoc.getElementsByTagName("author")[0]

#documents = author.getElementsByTagName("document")

#f=open("./output.txt", 'w')
#for document in documents:
#    firstchild = document.firstChild.data
#    print(firstchild)
#    f.write(firstchild + "\n")
#f.close()
    


