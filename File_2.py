
myfile=open(r'./ResultFolder/abc.txt','w')
myfile.write('india1234 gjgjhgjgjgjhgjhgjb ./n')
myfile.close()

myfile=open(r'./ResultFolder/abc.txt','r')
print (myfile.read())
myfile.close()
