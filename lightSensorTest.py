#!/usr/bin/env python3 -u
from ev3dev.ev3 import *


frontLight = LightSensor('in1')

backLight = ColorSensor()
backLight.mode = 'COL-COLOR'

print("front", frontLight.reflected_light_intensity, "back", backLight.color)
