#!/usr/bin/env python3 
from time import sleep 
from ev3dev2.motor import MediumMotor, MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor, GyroSensor
from ev3dev2.sound import Sound
from sys import stderr 

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C) 
sound = Sound()
ts = TouchSensor() 
cl = ColorSensor()
us = UltrasonicSensor() 

sound.speak('Find color')

# 0: No color, 1: Black, 2: Blue, 3: Green, 4: Yellow, 5: Red, 6: White, 7: Brown

find_color = 'Green'
print('find color : {0}'.format(find_color), file=stderr) # print to VS Code output panel

tank_drive.on(10,10)
while not cl.color_name == find_color:
    print(cl.color_name, file=stderr)
    sleep(0.1)

tank_drive.off()        # 정지
sound.speak('I found {0} color'.format(find_color))