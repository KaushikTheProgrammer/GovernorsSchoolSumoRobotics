#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
import time

rightMotor = LargeMotor('outA')
leftMotor = LargeMotor('outD')
rotationMotor = MediumMotor('outB')


backLight = ColorSensor()
backLight.mode = 'COL-REFLECT'

touchSensor = TouchSensor()

ultrasonicSensor = UltrasonicSensor()
ultrasonicSensor.mode = 'US-DIST-CM'

rotationMotor.reset()

direction = False
targetDistance = 0

def rotateRight(encoderCount):
    leftMotor.run_to_rel_pos(position_sp=-encoderCount, speed_sp=200, stop_action='hold')
    rightMotor.run_to_rel_pos(position_sp=encoderCount, speed_sp=200, stop_action='hold')
    rightMotor.wait_until_not_moving()
    leftMotor.wait_until_not_moving()


while True:
    val = backLight.value()
    if val >= 6:
        # Rotate robot at random number of degrees
        leftMotor.run_to_rel_pos(position_sp=-150, speed_sp=150, stop_action='hold')
        rightMotor.run_to_rel_pos(position_sp=-150, speed_sp=150, stop_action='hold')
        rightMotor.wait_until_not_moving()
        leftMotor.wait_until_not_moving()
        rotateRight(175)
    else:
        # Move straight
        if touchSensor.is_pressed:
            rightMotor.run_forever(speed_sp=900)
            leftMotor.run_forever(speed_sp=900)
        else:
            rightMotor.run_forever(speed_sp=400)
            leftMotor.run_forever(speed_sp=400)
            
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
            
            targetDistance = ultrasonicSensor.distance_centimeters

            if targetDistance < 35:
                

