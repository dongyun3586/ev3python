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

sound.speak('I am ready')

# while True:
#     print(cl.reflected_light_intensity)
#     sleep(1)
    
# region ColorSensor Mode
sound.speak('ambient light mode')
while not ts.is_pressed:
    print(cl.ambient_light_intensity) 
    print(cl.ambient_light_intensity, file=stderr)                # 반사광 측정값 출력

sound.speak('reflected light mode')
while not ts.is_pressed:
    print(cl.reflected_light_intensity) 
    print(cl.reflected_light_intensity, file=stderr)                # 반사광 측정값 출력

sound.speak('color mode')
while not ts.is_pressed:
    print("{0}({1})".format(cl.color_name, cl.color), file=stderr)  # 측정된 색상 이름(색상 번호) 출력
    sound.speak(cl.color_name)

sound.beep()    # 종료 비프음
# endregion