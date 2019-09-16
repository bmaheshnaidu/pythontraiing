'''
Regular expression:

This regular expression is also called as "RegEx" 
This is used to extract the data based on the "Pattern"
RegEx101.com is a site where we can learn regular expression

Character Set ==[]
[A-Z][a-z][0-9]=== and
[A-Za-z0-9] === or

include special characters :  " \special character  "
Any number of characters excpt new line:" * "

Package Name of regular expression is "RE"
''''' \
# print("Regular expression")

import re
data ="my email is abc1.xyz2@tcs.com  abc1.xyz22@tcs.com"
pattern="[a-z0-9]*\\.[a-z0-9]*\\@[a-z]*\\.com"
print(re.findall(pattern,data))
print(re.search(pattern,data))
print(re.search(pattern,data).group())
''' it returns the data of the matched string'''
print(re.search(pattern,data).start())
''' returns the starting position of the macth'''
print(re.split("\\s",data,1))
print(re.split("\\s",data))
print(re.split("\\s",data))

data="AB65BC7DC335"
moddata =re.sub("[A-Za-z]","@",data)
print (moddata)
modresult=re.split("@",moddata)
temp=0
for x in modresult:
    if x.isdigit():
        temp= temp+int(x)
        print(x)
print (temp)

''' returns the first word of the split'''
'''
findall()  -- this method will traverse whole string and extract all matching data.
search() -- this method will return only the frist occurance , it will return first cocurance starting position and ending position  for the macth in the attribute called "span", and it also returns the matched data in the attribute called "match:
to extract the data from search we need to use group() method is used
split() -- this methdod is split the string according to eh pattern
sub() -- find and replace the string with the pattern provided
for Number of occurrances {} is used
'''
data ="MY PAN NUMBER IS HYZPM4G00E"
pattern="[A-Z]{5}[0-9]{4}[A-Z]{1}"
print (data.findall(pattern,data))

