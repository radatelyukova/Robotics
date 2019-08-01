################################################################################
#   app_config.py
#
#   App configuration:
#       - reads input data
#       - tests conection to Raspberry Pi
#
#   01.00.2019  Created by:  rada
################################################################################
import os
import sys
import yaml

from lib.tools import *

class AppConfig():
    def __init__(self):
        params = self.read_values()
        print(params)
    
    def read_values(self, file_name='config/params.yml'):
        with open(file_name, 'r') as stream:
            try:
                return(yaml.safe_load(stream))
            except yaml.YAMLError as error_message:
                log(error_message)
                sys.exit('Failed to read params')
            
     