'''
1. create a excel having 5 columns  with 15 rows
emp_id, emp_companyName,emp_location,emp_project,emp_salary

2. Read the data from excel and insert data into the database

3.pre condition: create database with empdetails
create table name as emp_data

'''

import xlrd
import pyodbc

def connectDB():
    global cnxn
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-FPV9KKL\SQLEXPRESS;"
                      "Database=Emp_data;"
                      "Trusted_Connection=yes;")
    print("DB connection established succesfully")


def insertdata(emp_id,emp_companyname,emp_location,Emp_porject,Emp_salary):
    sqlquery="INSERT INTO[dbo].[Emp_details]([Emp_ID] , [Emp_companyname] , [Emp_location], [Emp_project], [Emp_salary]) VALUES ('{oemp_id}','{oemp_companyname}','{oemp_location}','{oemp_project}','{oemp_salary}')"
    data=sqlquery.format(oemp_id=emp_id,oemp_companyname=emp_companyname,oemp_location=emp_location,oemp_project=Emp_porject,oemp_salary=Emp_salary)
    cursor = cnxn.cursor()
    cursor.execute(data)
    cnxn.commit()

workbook = xlrd.open_workbook(r"C:\Users\bmahe\PycharmProjects\pythontraining\ResultFolder\Emp_details.xlsx")
worksheet = workbook.sheet_by_name("Emp_details")

connectDB()


for i in range(1,worksheet.nrows):
    emp_id=int(worksheet.cell_value(i,0))
    emp_companyname=str(worksheet.cell_value(i,1))
    emp_location = str(worksheet.cell_value(i, 2))
    emp_projectname = str(worksheet.cell_value(i, 3))
    emp_salary = int(worksheet.cell_value(i, 4))
    insertdata(emp_id,emp_companyname,emp_location,emp_projectname,emp_salary)






