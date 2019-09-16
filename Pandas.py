'''
Pandas:

unstructured  data -- table structure data
Tables are called as data frames
.loc method is used to fetch the data from the table.

Pandas is the package available in the python , which helps the users to convert the unstructed data into table structure data.

steps to install pandas
pip install pandas

Note: when we structized a data a atuo increment would be assigned to a data set

loc method is used to read the data row on a dataframe ie .loc[index number] eg .loc[0]

'''
import pandas as pd

emp_wages={"Employee Name":{"Rahul","Krish","Shantan","Ved"},
           "Location":{"KPHB","JNTU","Housing Board","kutkapally"},
           "Salary":{"1000","5000","2000","7000"}
           }

#print(pd.DataFrame(emp_wages))
emp_wages={"Employee Name":["Rahul","Krish","Shantan","Ved"],
           "Location":["KPHB","JNTU","Housing Board","kutkapally"],
           "Salary":["1000","5000","2000","7000"]
           }

#print(pd.DataFrame(emp_wages))

structued_data=pd.DataFrame(emp_wages)
#print (structued_data.loc[0])
#print (structued_data.loc[1])
#print (structued_data.loc[2])
#print (structued_data.loc[3])
#print(structued_data.count())
'''
filtering a data frame based on the data.
syn: dataframe.loc[dataframe[columnname]=="<value>"]

'''
print (structued_data.loc[structued_data["Employee Name"]=="Rahul"])
print (structued_data.loc[structued_data["Salary"]>="5000"])

