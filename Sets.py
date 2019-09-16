"""
Sets:

non indexed
unordered
not allows duplicate
iteritable
can update
can remove
can link(or) union with other set
represents wit {}
comma is a delimiter
"""

myset={"Raj","Rahul","Mahesh"}
print (myset)
for x in myset:
    print(x)

myset.add("krisna")
print(myset)
'''
undetermine element will be popped out.

'''
myset.pop()
print(myset)
'''
remove method is used to remove element for a specified value
'''
myset.remove("Raj")
print(myset)
'''
when we try to remove a value from the set, if value exist it will remove else keyerror will be raised
'''
myset.discard("krisna")
print (myset)

'''


'''
myset1={"rajul","raj","kumar"}
myset2={"1","2","3","raj"}

myset1.update(myset2)
print(myset1)
'''
union methos will take the smaller set values
'''
myset1={"rajul","raj","kumar"}
myset2={"1","2","3","raj"}

myset2.union(myset1)
print(myset2)

