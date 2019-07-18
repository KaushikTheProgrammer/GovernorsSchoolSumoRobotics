#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from time import sleep

rightMotor = LargeMotor('outA')
leftMotor = LargeMotor('outD')


rightMotor.run_forever(speed_sp=900)
leftMotor.run_forever(speed_sp=900)
time.sleep(7)

rightMotor.stop(stop_action='brake')
leftMotor.stop(stop_action='brake')
