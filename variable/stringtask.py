mystr ="the global id is:1537 the trans code is : 23456 the journal number : 27809"
temp=""
for i in range (0,len(mystr)):
    if (i+1 != len(mystr)):
        if (mystr[i].isdigit() and mystr[i+1].isspace()):
            temp=temp+mystr[i]+"@"
        else:
            temp= temp+mystr[i]
    else:
        temp = temp + mystr[i]
arr = temp.split("@")
'''
.strip() function is used to remove the space in the front of the statement
.capitalize method is used capitalize of the statment
.findandindex method is used to find and index 
.find method is used to get the index position of a given word in the source string, when a match is found it will return the interger value >=0 else -1
 note: this method will return the first occurance of the word
.index method it will also work like find only but if there is matches available it will throw an exception

'''
for word in arr:
    print(word.strip().capitalize())


str="my voucher number is (12345)"

pos1=str.find ("(")+1
pos2=str.find(")")
print(str[pos1:pos2])


str="my voucher number is :12345"
colpos1=str.find (":")+1
''' if second index is empty means, will get the enter string from the first index position'''
print (str[colpos1:])

'''rfind or rindex
rfind method is used to the find the first occurrence from the right side to the left side
'''
str="E:\\string\\output\\string_output"
pos =str.rfind(("\\"))+1
print(str[pos:])
pos =str.find(("\\"))+1
print(str[pos:])

'''
isalnum() function is used to give boolen value if the value is alpha numberic
zfill() method would be used to append zero for the number of lenght., if the lenght of the string is eaual to the len then zero would not append
'''
str="hello"
print (str.zfill(30))
