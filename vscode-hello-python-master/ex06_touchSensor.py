#!/usr/bin/env python3 
from time import sleep 
from ev3dev2.sound import Sound
from ev3dev2.motor import MediumMotor, MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, UltrasonicSensor
from sys import stderr 

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
spkr = Sound()
spkr.speak('I am ready')
ts = TouchSensor() 

while not ts.is_pressed:
    sleep(0.1)

spkr.speak('Touch sensor button is pressed')










