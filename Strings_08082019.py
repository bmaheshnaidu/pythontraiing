# cast function STR() int() float()
# int_x = int_x+10 or int_x += 10
# arithmetic operators( +,-,*,/)
# assignment operators (=)
# comparision operators ( ==, >,<,>=,<=, !=)
# membership operators (in, not in)
# identification operators ( is , is not)
# logical operator ( and, or, not, xor)
# Bit wise operator ( &, | , ~)
# Logical statements or conditional statements (if, if else, elif)  No switch case in python
#

int_x = 10
int_x = int_x+10
int_x += 10
x,y =10,20
print(x,y)

if x > y:
    print("x is greater than y  and value of x is :{0} and y value is :{1}".format(x,y))
else:
    print("y is greater than x  and value of x is :{0} and y value is :{1}".format(x,y))

if x > y:
        print("x is greater than y  and value of x is :{xvalue} and y value is :{yvalue}".format(xvalue=x, yvalue=y))
else:
        print("y is greater than x  and value of x is :{xvalue} and y value is :{yvalue}".format(xvalue=x, yvalue=y))

# when we want to display int value along with string msg us format method with index
# when we have multiple values to be integrated along with the string msg then go by value based arguments

