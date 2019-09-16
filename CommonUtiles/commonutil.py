import re
import datetime

def extractPattern_data(sourcestring,pattern):
    return re.findall(pattern,sourcestring)

def getSystemdatetime():
    return datetime.datetime.now()