#!/usr/bin/env python3 -u
from ev3dev.ev3 import *

touchSensor = TouchSensor()

while True:
    if touchSensor.is_pressed:
        print("being pressed")
    else:
        print("not beign pressed")


