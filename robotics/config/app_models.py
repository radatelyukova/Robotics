################################################################################
#   app_models.py
#
#   <Module Purpose>
#
#   10.08.2019  Created by: rada
################################################################################
from models.host import *

class AppModels():
    def __init__(self, config):
        self.host = Host(config.addr, config.name, config.user)
        