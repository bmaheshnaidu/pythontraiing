empdetails={"":""}
print (type(empdetails))
x=1
while x<=15:
    empdetails[x]={"Name": "Name"+str(x), "Place":"Place"+str(x)}
    x+=1


myfile=open(r'./ResultFolder/New.txt','w')
# x=1
# while x<=15:
#     myfile.write(str(empdetails[x]))
#     x+=1
myfile.write(str(empdetails))
myfile.close()
myfile=open(r'./ResultFolder/New.txt','r')
print (myfile.read())
myfile.close()





