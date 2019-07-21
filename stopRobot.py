#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

rightMotor = LargeMotor('outD')
leftMotor = LargeMotor('outA')
rotationalMotor = MediumMotor('outB')

rightMotor.run_forever(speed_sp=0)
leftMotor.run_forever(speed_sp=0)
rotationalMotor.run_forever(speed_sp=0)
