#!/usr/bin/env python3 -u
from ev3dev.ev3 import *


#frontLight = LightSensor()

backLight = ColorSensor()
backLight.mode = 'COL-REFLECT'

while True:
    print(backLight.value())
    #print("back", backLight.color)
    #print("front", frontLight.reflected_light_intensity, "back", backLight.color)
