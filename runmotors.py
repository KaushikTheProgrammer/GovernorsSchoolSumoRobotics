#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from time import sleep

rightMotor = LargeMotor('outA')
leftMotor = LargeMotor('outD')
rotation = MediumMotor('outB')

direction = False

rotation.reset()
while True:
    print(rotation.position)
    if rotation.position > 126:
        direction = False
    elif rotation.position < -126:
        direction = True
    
    if not direction:
        rotation.run_to_rel_pos(position_sp=-10, speed_sp=100, stop_action='hold')
        rotation.wait_until_not_moving()
    else:
        rotation.run_to_rel_pos(position_sp=10, speed_sp=100, stop_action='hold')
        rotation.wait_until_not_moving()
