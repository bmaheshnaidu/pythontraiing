''' JSON -- Java Script Object Notation

JSON is a very light weighted file
1. Easy to read
2.Easy to communicate with other systems developed on other technologies
3.dump
4.load
5. import your json
6. json.dumps(jscon object,sort_keys=true)
7. json object converts into string object
'''
#step 1
import json
#step 2
dumpdata={
    "Name":"pratap",
    "Age":"29",
    "place" : "Hyderabad",
    "location": "kukatpally"
}

#step 3

jsonfile=open(r'./ResultFolder/testdatas.json','w')

#step 4
jsondumpdata=json.dump(dumpdata,jsonfile,ensure_ascii=False,indent=4)
jsonfile.close()

jsonfile=open(r'./ResultFolder/testdatas.json','r')
print (jsonfile.read())
jsonfile.close()
