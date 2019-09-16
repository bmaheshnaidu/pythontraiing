'''
Tuples: unchangeable collection items
can't change the value
A tuple can be convert into other data type collection object
tuple allows to retrieve the data based on index position
tuple allow reverse indexing to fetch the data
tuple can ebe iterable over a loop
tuple allows membership operator
a single vale represents in a tuple will not treat as tuple, we must give a comma

'''

mytuple=('Raj','Ram','Hari')
#to know the type
print (type(mytuple))

print (mytuple)
#to retrive the tuple value
print(mytuple[1])
# -1 represents last elements , to get the reverse indexing
print (mytuple[-1])
print (mytuple[-2])

#to update the data, tuple is not changeable, when we try to assign it trows a erorrs , tuple does not support item assignment
# mytuple[0]="rakesh"  it trows an error.

for x in mytuple:
    print(x)
# if we don't give comma seperator it consider as string
mytuple=("ram")
print(type(mytuple))
# to represents as tuple we need to give comma
mytuple=("ram",)
print(type(mytuple))

# a tuple can't be clear..,

mytuple=("ram","raj","hari")
# mytuple.clear() it throws error
# to delete a tuple, will use the keyword del to remove from the memory
del mytuple

'''
Dictionary is represents in the key value pair
'''
odict={"username":"pratap","password":"12345"}
print (odict)
print (type(odict))

print(odict["username"])
print(odict["password"])
print(odict.get("username"))
# value will be updated with the key
odict["password"]="6779"
print (odict)
# adding an item to dictionary
odict["url"]="https://yahoo.com"
print (odict)

#deletion on dictionary  pop, popitem and delete will be use to delete.
#
print (odict.pop("password"))
print (odict)
# to delete the last item from the dictionary will use popitem()
print (odict.popitem())
print (odict)

del odict

# when we loop it will return the key not the value
odict={"username":"pratap","password":"12345"}
for x in odict:
    print(x)
    print(x + ' ' + odict[x])
# to retrive key and vale from the dictionary
for k,v in odict.items():
    print (k,v)


mystr="india has many hotels in india in manufacturs"
arr=mystr.split(" ")
print (arr)
mynewstr=[]
mynewdic={}
count=0
for item in arr:
    if (item not in mynewstr):
        mynewstr.append(item)
        print(item + ' ' + str(mystr.count(item)))
        mynewdic[item]= mystr.count(item)
print (mynewstr)
print (mynewdic)

