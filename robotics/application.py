################################################################################
#   ~.py
#
#   <Module Purpose>
#
#   25.06.2019  Created by: rada
################################################################################
from   tkinter import *

from config.app_config import *
from config.app_models import *

class Application():
    def __init__(self):
        config = AppConfig()
        models = AppModels(config)
        debug(models)
        