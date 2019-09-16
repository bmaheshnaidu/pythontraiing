'''# looping statements
# In Python we have 2 looping "for loop" and "while loop"

for x in range(1, 10):
     print (x)

# To extact each and every character in the given string
str1="india"
for x in str1:
    print(x)

# break statement, Break is a keyword which is used it to exist from a loop based on a condition

for x in range(1, 10):
    # print (x)
    if (not x==5):
        print (x)
    else:
        break;

#"welcome to the python training"
y=0
z=0
str1="welcome to python training"

for x in str1

    if x in ("a","e","i","o","u"):
        y=y+1
    else:
        z=z+1

print ("number of vowels " +str(y))
print ("number of consoents " +str(z))
'''
patern="*"
temp=""
for x in range (1,6):
    for c in range (1,x+1):
        temp+=patern
    print (temp)
    temp=""

'''patern="school"
temp=""
for x in range (1,len(patern)):
    for c in range (1,x+1):
        temp+ =x
    print (temp)
    temp=""  '''''

x=10
y=20
x=x+y
y=x-y
x=x-y
print (x)
print (y)