################################################################################
#   tools.py
#
#   Common functions
#
#   25.00.2019  Created by:  rada
################################################################################
from pprint import pprint
from sys import exit
from time import *

def debug(object):
    pprint(vars(object))

def log(message):
    print(strftime("%Y-%m-%d %H:%M:%S %Z", localtime(time())), message)

def quit():
    log("Completed")
    exit(0)