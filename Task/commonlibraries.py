import re

def load_getdata (path):
    file=open(path,"r")
    return file.read()

def extractPattern_data(sourcestring,pattern):
    return re.findall(pattern,sourcestring)

