'''

configuration file is a place holder where user can able to store the different environments like dev, integration ,BAT,QA etc.
Each environment will have different configurations

Depends upon the user criteria, python code should pick the appropriate section level details.

extension for this configuration file is .cnf

package name is configparser

data would be fecth from configparser only

'''


import configparser
config = configparser.RawConfigParser()
configFilePath = r"C:\Users\bmahe\PycharmProjects\pythontraining\environment.cnf"
config.read(configFilePath)
print(config.get("qa","url"))
print(config.get("dev","url"))
print(config.get("qa","username"))
print(config.get("qa","pwd"))


#envdetails=config.read(filepath)
#print (envdetails)

