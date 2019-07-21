#!/usr/bin/env python3
################################################################################
#   01.py
#
#   Ex. 01: Motor spin
#
#   04.06.2019  Created by:  rada
################################################################################

from gpiozero import Motor
from time import sleep

motor_right = Motor(forward=12, backward=6) 

while(True):
    try:
        motor_right.forward(0.7)
        sleep(3)
        motor_right.backward(0.3)
        sleep(3)
        
    except:
        print('Job has been aborted')
        motor_right.stop()
        break