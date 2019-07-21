#!usr/bin/env python3 -u

from ev3dev.ev3 import *


ultrasonicSensor = UltrasonicSensor('in3')
ultrasonicSensor.mode = 'US-DIST-CM'

rightMotor = LargeMotor('outA')
leftMotor = LargeMotor('outD')
panMotor = MediumMotor('outC')




print(ultrasonicSensor.distance_centimeters)
