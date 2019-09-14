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
        self.initialize_host(params)
        self.initialize_models(params)
        
    def initialize_host(self, params):
        self.addr = params['host']['addr']
        self.name = params['host']['name']
        self.user = params['host']['user']

        self.test_connection()

    def initialize_models(self, params):
        if ('leds') in params:
            self.leds = params['leds']
            print(self.leds)
            
    def read_values(self, file_name='config/params.yml'):
        try:
            with open(file_name, 'r') as stream:
                return(yaml.safe_load(stream))
        except OSError as error_message:
                log(error_message)
                sys.exit('File not found')
        except yaml.YAMLError as error_message:
                log(error_message)
                sys.exit('Failed to read params')
                
    def test_connection(self):
        response = os.system("ping -c 1 " + self.addr)
        if response == 0:
            log('Connection is ok')
        else:
            sys.exit('Connection failed')
            