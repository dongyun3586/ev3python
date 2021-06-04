#!/usr/bin/env python3
from sys import stderr
from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import SpeedRPS, SpeedRPM, SpeedDPS, SpeedDPM

sound = Sound()
mm = MediumMotor()
lm = LargeMotor(OUTPUT_C)   # 연결 포트를 지정 안하면 기본 포트로 동작

sound.speak('I am ready')

# mm.on_for_degrees(20, 90)   # 위로 올라감
# sleep(1)
# mm.on_for_degrees(20, -90)  # 아래로 내로옴

# while mm.wait_until_not_moving(timeout=1):
#     mm.on(-30)
# sound.speak('I do not move')
# sleep(1)

# while mm.wait_until_not_moving(timeout=1):
#     mm.on(30)
# sound.speak('I do not move')
# sleep(1)

# while mm.wait_until_not_moving(timeout=1):
#     mm.on(-30)
# sound.speak('I do not move')
# sleep(1)

# while mm.wait_until_not_moving(timeout=1):
#     mm.on(30)
# sound.speak('I do not move')
# sleep(1)

# while mm.wait_until_not_moving(timeout=1):
#     mm.on(-30)
# sound.speak('I do not move')



sound.beep()




