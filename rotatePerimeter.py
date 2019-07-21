#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

rightMotor = LargeMotor('outA')
leftMotor = LargeMotor('outD')

backLight = ColorSensor()



def rotateRight(encoderCount):
    leftMotor.run_to_rel_pos(position_sp=-encoderCount, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=encoderCount, speed_sp=200, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()

def moveStraight():
    rightMotor.run_forever(speed_sp=200)
    leftMotor.run_forever(speed_sp=200)
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()

while True:
    val = backLight.color
    print(val)
    if val == 2:
        # Rotate robot at random number of degrees
        rightMotor.run_forever(speed_sp=-200)
        leftMotor.run_forever(speed_sp=-200)
        rightMotor.wait_until_not_moving()
        leftMotor.wait_until_not_moving()
        rotateRight(175)
    else:
        # Move straight
        rightMotor.run_forever(speed_sp=200)
        leftMotor.run_forever(speed_sp=200)
