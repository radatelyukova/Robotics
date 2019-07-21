#!/usr/bin/env python3
################################################################################
#   01.py
#
#   Ex. 02: square motion
#
#   04.06.2019  Created by:  rada
################################################################################

from gpiozero import Robot
from time import sleep

robot = Robot(left=(27,22), right=(18,17))

for i in range(4):
    robot.forward(0.7)
    sleep(1)
    robot.right()
    sleep(0.3)
    
robot.stop()
