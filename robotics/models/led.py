################################################################################
#   led.py
#
#   Class LED
#   
#   Arguments:
#       color   - LED color
#       gpio    - GPIO pin to conect LED
#       factory - GPIO pins factory
#
#   14.09.2019  Created by:  rada
################################################################################
import gpiozero as GPIO

class LED():
    def __init__(self, color, gpio, factory):
        self.color   = color
        self.gpio    = gpio
        self.factory = factory
        
    def get_attr(self):
        return(self.color, self.gpio, self.factory)