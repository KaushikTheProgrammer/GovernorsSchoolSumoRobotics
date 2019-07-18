#!/usr/bin/env python3 -u
from ev3dev.ev3 import *
from time import sleep

m1 = LargeMotor('outA')
m2 = LargeMotor('outD')

m1.run_forever(speed_sp=900)
m2.run_forever(speed_sp=900)
time.sleep(7)

m1.stop()
m2.stop()
