#!/usr/bin/env python3
################################################################################
#   01.py
#
#   Ex. 01: simple motion
#
#   03.06.2019  Created by:  rada
################################################################################

from gpiozero import Robot
from time import sleep

robot = Robot(left=(6,12), right=(22,23))

for i in range(2):
    robot.forward(0.5)
    sleep(2)
    robot.left(0.4)
    sleep(0.5)
    
robot.stop()
