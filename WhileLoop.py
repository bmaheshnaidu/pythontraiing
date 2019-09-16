'''

when the loop is indefinite:
 problems:
    No break down
    Memory leaks
    System halt or corrupt

'''

i=1
while i <= 10:
    if (i!=5):
        print("values from while " + str (i))
        i += 1
    else:
        break

# continue is the keyword which is used to skip set of statements based upon the condition

for i in range (1,10):
    if(i==5):
        continue
    print (2*i)


