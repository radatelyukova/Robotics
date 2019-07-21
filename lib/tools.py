################################################################################
#   tools.py
#
#   Command: functions
#
#   25.00.2019  Created by:  rada
################################################################################

from sys import exit
from time import *

def log(message):
    print(strftime("%Y-%m-%d %H:%M:%S %Z", localtime(time())), message)

def quit():
    log("Completed")
    exit(0)