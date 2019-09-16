import re
duplicatechar=[]
mystr="welcome to phyton training"
mystr=re.sub('\s*','',mystr)
print(mystr)
for x in mystr:
    if (mystr.count(x)>1) :
        duplicatechar.append(x+"  " + str(mystr.count(x)))
print (duplicatechar)
x=len(mystr)
print(x)
statement=(((x/2)%2==0))
print(statement)
if statement:
    value=(x/2)-1
else:
    value=int(x/2)+1
print(mystr[value])

## source tree, git batch for windows, account in git hub, visual studio code

