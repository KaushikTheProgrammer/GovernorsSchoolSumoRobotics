#!usr/bin/env python3 -u
from ev3dev.ev3 import *


rightMotor = LargeMotor('outA')
leftMotor = LargeMotor('outD')

rightMotor.run_to_rel_pos(position_sp=125, speed_sp=100, stop_action='hold')
leftMotor.run_to_rel_pos(position_sp=-125, speed_sp=100, stop_action='hold')

