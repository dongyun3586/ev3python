#!/usr/bin/env python3
from time import sleep 
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.motor import SpeedRPS, SpeedRPM, SpeedDPS, SpeedDPM
from ev3dev2.sound import Sound

spkr = Sound()
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# 1. 회전수로 제어: on_for_rotations(left_speed, right_speed, rotations, brake=True, block=True) 
tank_drive.on_for_rotations(50, 50, rotations=2)   # 1바퀴 = 17.58cm
spkr.speak('Rotations Test Completed')

# 2. 각도로 제어: on_for_degrees(left_speed, right_speed, degrees, brake=True, block=True) 
tank_drive.on_for_degrees(10, 10, degrees=720)   # 17.58cm
spkr.speak('Degrees Test Completed')

# 3. 시간(초)으로 제어: on_for_seconds(left_speed, right_speed, seconds, brake=True, block=True) 
tank_drive.on_for_seconds(50, 50, seconds=3)   # 시간 = 거리/속도
spkr.speak('Seconds Test Completed')

# 4. 계속 회전: on(left_speed, right_speed) 
# tank_drive.on(50, 50) 
# sleep(2) 
# tank_drive.off()