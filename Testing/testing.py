'''
consuming other class properties into another class

syn : from <DirectoryName> import <filename>
eg: from CommonUtiles import commonutil

to provide alias name
syn : from <DirectoryName> import <filename> as <aliasname>
eg: from CommonUtiles import commonutil as lib

__int__ is used as initialization file, when we give it as a name to a file, it convert directory into modules
Note: no logic is required to write in the int file

collection: phyton has different collection has list, tuple, set, dictionary
List: order and indexed and changeable
    1. Duplicates allowed
    2. represents with []
Tuple: order and indexed and not changeable
    1. Duplicates allowed
    2.represents with ()
Set: un-order and no indexed position
    1.No duplicates allowed
    2.represents with {}
Dictionary: key value and pairs
    1.No duplicate keys allowed
    2.represents with {}

'''
from CommonUtiles import commonutil
from CommonUtiles import commonutil as lib
# without specifing the folder naem using from keyword
import CommonUtiles.commonutil as libray
print(commonutil.getSystemdatetime())
print(lib.getSystemdatetime())
print(libray.getSystemdatetime())
