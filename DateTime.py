'''
datetime package is used for datetime functions
'''

import datetime
print (datetime.datetime.now())
currentdate=datetime.datetime.now()
print(currentdate)
print(datetime.datetime.today())
print(currentdate.year)
print(currentdate.month)
print(currentdate.day)
print(currentdate.weekday())

# formating the datetime, strftime() method is used
print(currentdate.strftime("%A"))
print(currentdate.strftime("%b"))
#print (datetime.datetime(yyyy,mm,dd))
print(datetime.datetime(2017,2,5))



'''
converting directory as a modules

'''

