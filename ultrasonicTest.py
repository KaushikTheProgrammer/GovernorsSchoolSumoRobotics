#!usr/bin/env python3 -u

from ev3dev.ev3 import *


ultrasonicSensor = UltrasonicSensor()
ultrasonicSensor.mode = 'US-DIST-CM'

while True:
    print(ultrasonicSensor.distance_centimeters)
