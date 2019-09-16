import json
filedata=open(r'./ResultFolder/testdatas.json','r')
#print (filedata.read())
#tempstr=json.load(filedata)
#print(tempstr)
print(json.load(filedata))
filedata.close()