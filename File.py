'''
File System:

what operation?
    file management on various format .txt,.xlxs,.pdf,.jcom
    folder management
    WAX -- write, append and raise an error when file exist

To write a file in python the method "open" . Open has two parameters, first one file path and second one mode of operation
w -- Writing a file, when there is no file it will create a file
a --
x
r -- for reading a file
when we do not mention the path of the file, it will take the current execution base script path

'''

myfile=open(r'abc.txt','w')
myfile.write('india')
myfile.close()

# writing a file into a relative path under project directory
myfile=open(r'./ResultFolder/abc.txt','w')
myfile.write('india1234gjgjhgjgjgjhgjhgjb ./n')
myfile.write('india5431234gjgjhgjgjgjhgjhgjb ./n')
myfile.write('india1sdfsd234gjgjhgjgjgjhgjhgjb ./n')
myfile.write('india12dfdsf34gjgjhgjgjgjhgjhgjb ./n')

myfile.close()

#reading  a file into a relative path under project directory
# To read a file method name is read()
myfile=open(r'./ResultFolder/abc.txt','r')
print (myfile.read())
myfile.close()
# to read specific number of character read(character_number)
myfile=open(r'./ResultFolder/abc.txt','r')
print (myfile.read(5))
myfile.close()

# to read line by lien readline()
myfile=open(r'./ResultFolder/abc.txt','r')
print (myfile.readline())
myfile.close()

myfile=open(r'./ResultFolder/abc.txt','r')
x=myfile.readline()
while (len(x)>0):
    print (x)
    x=myfile.readline()

print (myfile.readline())
myfile.close()
