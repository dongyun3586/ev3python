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
leds = Leds()

sound.speak('I am ready')
leds.all_off() # stop the LEDs flashing (as well as turn them off)
while not ts.is_pressed:
    if us.distance_centimeters < 40: # to detect objects closer than 40cm
        # In the above line you can also use inches: us.distance_inches < 16
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
    else:
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')
        
    print(us.distance_centimeters, file=stderr)
    sleep(1)

sound.beep()







