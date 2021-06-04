#!/usr/bin/env python3 
from time import sleep 
from ev3dev2.motor import MediumMotor, MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor, GyroSensor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from sys import stderr 

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C) 
sound = Sound()
ts = TouchSensor() 
cl = ColorSensor()
us = UltrasonicSensor() 

sound.speak('Move')

while not ts.is_pressed:
    print(cl.reflected_light_intensity, file=stderr)
    sleep(0.1)
 
def move(left_speed, right_speed):
    tank_drive.on(left_speed, right_speed)

while not ts.is_pressed:
    if cl.reflected_light_intensity > 55:
        move(60, 20)
    else:
        move(20, 60)

tank_drive.stop()
sound.beep()













