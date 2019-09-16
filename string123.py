'''

string are called as self implemented arrays in pyhton only
when we speak on arrays, we generally called as same set of  data type items
arrays will work based on indexing , index will start from 0
'''
'''
mystr="india"
print(mystr[1])

# To reverse a string
print (mystr[::-1])

mystr=" my emplyee id 21"
revstr=mystr[::-1]

# croping  a string
print (revstr[0:2])
# reverse the string
print (revstr[0:2][::-1])
mystr="SCHOOL"
i=0
while (i<= len(mystr)):
    print (mystr[0:i])
    i+=1;

for i in range(0,len(mystr)+1):
    print(mystr[0:i])

uservalue=input("Enter a string to print : ")
for i in range(0,len(uservalue)+1):
    print(uservalue[0:i])

uservalue=input("Enter a value : ")
for i in range (1,21):
    print("{0} * {1} = {2}".format(uservalue,i,(int(uservalue)*i)))
    
'''
'''
Count: this method is used to get the count of a caharacter pr a word from the given source string

strVariable.count('character' or 'word')

mystr="india"

#print(mystr.count("i"))
for i in mystr:
    print (i + " repeated for " + str(mystr.count(i)))

'''''
# split method is used to break a string based on user given delimiter, when we break a string we will get a list of workds
# syntax: string or stringvariable.split("delimiter")
mystr="india has many hotels in india manufacturs"
arr=mystr.split(" ")
print (arr)
count=0
for item in arr:
    if (item=="india"):
        count +=1
print (count)

# to convert to case sensitive string variable.upper() or string variable.lower()
mystr="India has many Hotels in india manufacture"
mystr=mystr.upper()
print (mystr)
mystr="India has many Hotels in india manufacture"
mystr=mystr.lower()
print (mystr)
mystr="India has many Hotels in india manufacture"
mystr=mystr.swapcase()
print (mystr)
#casefold() is used to convert to lower
mystr="India has many Hotels in india manufacture"
mystr=mystr.casefold()
print (mystr)
#title() is used to convert to first character of word to Upper
mystr="India has many Hotels in india manufacture"
mystr=mystr.title()
print (mystr)
mystr="India has many Hotels in india manufacture"
mystr=mystr.capitalize()
print (mystr)
str="my traction id is : 108956"
arr =str.split(" ")
for item in arr:
    if (item.isdecimal()):
        print(item)
        break

str="my traction id is : 108N956"
arr =str.split(" ")
for item in arr:
    if (item.isalnum()):
        print(item)



