#!/usr/bin/env python3 -u
from ev3dev.ev3 import *


#frontLight = LightSensor('in1')

backLight = ColorSensor()

while True:
    print("back", backLight.color)
    #print("front", frontLight.reflected_light_intensity, "back", backLight.color)
