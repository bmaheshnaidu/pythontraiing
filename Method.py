'''

Method is a block of code where user will write all the business logic and use for th purpose of reuseabliity

Method always try to accept a value adn tries to return a value
Methods are called as behaviours

values which are accepted in the methods are called parameter.
values which are sending to the methods are called arguments

syntex:
def methodName(par1,par2,...):
Note:
1.Number of parameters must be equal to number of arguments
2.Value can be return with a keyword "return"
3. When a method has a returns then this method has to be assign to variable in order to store the return value.
4. When a variable is created inside a method ,variable is called as local variable
    1. All parameters are called a local variables
5.Local varaiable will not expose to the outer world, lifetime would be within the method
6. converting local  varaible to global variable, we will use "global" keyword is used
7.
'''
import re
import datetime
def add(a,b):
    print("I am adding two numbers " +str(a+b))
    return a+b
temp=add(10,20)
print (temp)

def add(a,b):
    global c
    c=a+b

add(10,20)
print (c)


def extractPattern_data(sourcestring,pattern):
    return re.findall(pattern,sourcestring)

data ="MY PAN NUMBER IS HYZPM4600E"
pattern="[A-Z]{5}[0-9]{4}[A-Z]{1}"
print (extractPattern_data(data,pattern))

date= "my dob is 09/08/1900"
pattern="[0-9]{4}"
print (extractPattern_data(date,pattern))


