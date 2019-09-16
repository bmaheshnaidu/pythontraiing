'''
python logging:

logging is an internal package available for tracing different levels of statement printing process

Logging levels that are available are

D-Debug -- This level can provide in detailed explanation of each statement
I-Info -- This will be used inside a method , which tells the user whether a method is processed or not
W-warning -- It will user to anticipate there might be a issue which may impact the system because of missing functionalities
E-error -- This level is used when a expected values are not appearing
C-critical -- When there is no work around exist to proceed further critical level is used.

Note: When user chooses any one of the logging level, levels before to that (preceeding) will never get access.
Levels which is choose by the user and after to that will only get access.
By default logging level is set to warning.

'''
import logging
#logging.basicConfig()
a=10
b=20
print("Sum of two number is {}".format(a+b))
logging.debug("Sum of two number is {}".format(a+b))
logging.info("Sum of two number is {}".format(a+b))
logging.warning("Sum of two number is {}".format(a+b))
logging.error("Sum of two number is {}".format(a+b))
logging.critical("Sum of two number is {}".format(a+b))
'''
setting information on the log files "asctime" -- human readable time
"funcName"--
"levelno" --


in this above exaple. logging level are temporary and it will not save permanently.

To have permanent logging methodology , we should configure few settings which filename and formats.

Log file must have the extension called .log

To set this configuration, method is logging.basicConfig()

'''
logging.basicConfig(filename="features.log",
                    format="%(asctime)s:%(levelname)s")


'''
create a instant to a logging class
using that instant, utilzer the method call getlogger 
'''
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
print (logger)
logger.debug("Sum of two number is {}".format(a+b))
logger.info("Sum of two number is {}".format(a+b))
logger.warning("Sum of two number is {}".format(a+b))
logger.error("Sum of two number is {}".format(a+b))
logger.critical("Sum of two number is {}".format(a+b))

