'''

configuration python with database

to connect to DB, python requires a package call pyodbc
to connect with any DB , user must have the following details
1. Driver : this will be different from DB to DB
2. Server:
3.Database: DB name
4.Trusted_Connection=yes this should be given as Yes , when DB is configured with windows authentication

cursor allows the user to execute the query statement,
query statment are two types, executive query and non executive query
executive query will return back a value or statement
non executive query will not return back the statement

cursor will always return a collection object where we need to iterate using a looping statement

username: sa passwword: password1234

'''

import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-FPV9KKL\SQLEXPRESS;"
                      "Database=Testing;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM table1')

for row in cursor:

    print('row = %r' % (row))

