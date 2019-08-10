################################################################################
#   host.py
#
#   Class Host
#   
#   Arguments:
#       addr - IP Adress
#       name - Host name
#       user - User (login)
#
#   10.00.2019  Created by:  rada
################################################################################
import gpiozero             as     GPIO
from   gpiozero.pins.pigpio import PiGPIOFactory


class Host():
    def __init__(self, addr, name, user):
        self.addr = addr
        self.name = name
        self.user = user
        
        self.factory = PiGPIOFactory(host=self.addr)
        GPIO.Device.pin_factory = self.factory         # Workaround: MUST BE!!!