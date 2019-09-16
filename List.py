'''
creating a list and printing the type
List is an heterogeneous type, which can accept any type of data

'''
mylist=[]
print(type(mylist))
mylist={}
print(type(mylist))
mylist=()
print(type(mylist))
# Adding listing and printing
mylist=["Apple","Orange","Banana",1,2,3]
print(mylist)

# adding Items to the existing list, whenever user adds an item or element to the list it will add to the last index

mylist.append("count")
print(mylist)
# Item can be retrrive from a list based on the index position

print(mylist[1])
# retriveing all the elemnts  using for loop
for item in mylist:
    print(item)

#Getting length of a list
print (len(mylist))
i=0
while i<len(mylist):
    print (mylist[i])
    i+=1

#updating an item in the existing list
mylist[1]="Fruit"
print (mylist)

#inserting a item in the middle of the list
mylist.insert(1,"mango")
print (mylist)

# merging a two list, a list can be extended with the keyword extend. eg: list1.extend(list2)
mylist=["Apple","Orange","Banana"]
mylist2=[4,5,6,1,2,3]
mylist.extend(mylist2)
print (mylist)
# To remove a item available at the last index
mylist.pop()
print (mylist)
# using this pop method we can also remove an item by specfied with index

mylist.pop(4)
print (mylist)
# remove method will always accepts object not index
# when there is no object exist in a list , it throws an value error
mylist.remove("Orange")
print (mylist)

# if an object exist in an list or not we will use member ship operator "in"
fruits=["apple","orange","mango"]
print ("list" in fruits)

# how to convert a string into a list
empname=("testing, the, value")
print(list(empname))

mystring="Welcome to phyton training1"
print (list(mystring))
temp=""
samechar=[]
for item in list(mystring):
    print (item)
    if item!=' ':
        temp=temp+item
        if not item in samechar:
            samechar.append(item)

print (temp)
print (samechar)
midchar=len(temp)/2
print(temp[int(midchar)])




# remove all space
# display only duplicate characters
# print the middle character in the string
