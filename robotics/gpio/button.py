#!/usr/bin/env python3
################################################################################
#   button.py
#
#   Button controle via GPIO
#
#   27.05.2019  Created by:  rada
################################################################################

from gpiozero import Button
from time import sleep

button = Button(17) 

while(True):
    try:
        if button.is_pressed:
            print('Button is on')
            sleep(1)
        else:
            print('Button is off')
            sleep(1)
    except:
        print('Job has been aborted')
        break