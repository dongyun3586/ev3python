#!/usr/bin/env python3
from time import sleep 
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.motor import SpeedRPS, SpeedRPM, SpeedDPS, SpeedDPM
from ev3dev2.sound import Sound

spkr = Sound()
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

spkr.speak('Move')

#region 1.스피드 20으로 1초동안 움직인 거리는?
# tank_drive.on_for_seconds(left_speed=20, right_speed=20, seconds=1, brake=True, block=True)

# speed = 10   # 1초 동안 움직인 거리가 10cm 라면
# spkr.speak('Move 5 centimeter')
# tank_drive.on_for_seconds(20, 20, seconds=5/speed)    # 5cm 움직이기
# spkr.speak('Move 20 centimeter')
# tank_drive.on_for_seconds(20, 20, seconds=20/speed)   # 20cm 움직이기
#endregion

#region 2.각도로 원하는 거리만큼 이동시키는 함수
# tank_drive.on_for_degrees(20, 20, degrees = 20.48 * 10)   # 360도 = 17.58cm, 1cm = 20.48도

# spkr.speak('Move 5 centimeter')
# tank_drive.on_for_degrees(20, 20, degrees = 20.48 * 5)

# spkr.speak('Move 20 centimeter')
# tank_drive.on_for_degrees(20, 20, degrees = 20.48 * 20)
#endregion

#region 3. 원하는 방향으로 원하는 거리만큼 움직이기
# direction = 'forward'   # 'backward'
# speed = 30              # 60
# distance = 10           # 5, 20

# if direction == 'forward':
#     tank_drive.on_for_degrees(speed, speed, degrees = 20.48 * distance)   # 360도 = 17.58cm, 1cm = 20.47도
# elif direction == 'backward':
#     tank_drive.on_for_degrees(-speed, -speed, degrees = 20.48 * distance)

# 20의 속도로 5cm 전진 시키기

# 60의 속도로 10cm 전진 시키기

# 40의 속도로 15cm 후진 시키기
#endregion

#region 4. move( ) 함수 만들기
def move(direction, speed, distance):
    msg = 'Move {0} {1} centimeter'.format(direction, distance)
    spkr.speak(msg)
    if direction == 'forward':
        tank_drive.on_for_degrees(speed, speed, degrees = 20.48 * distance)   # 360도 = 17.58cm, 1cm = 20.47도
    elif direction == 'backward':
        tank_drive.on_for_degrees(-speed, -speed, degrees = 20.48 * distance)

# 20의 속도로 5cm 전진 시키기
move('forward', 20, 5)

# 60의 속도로 10cm 전진 시키기
move('forward', 60, 10)

# 40의 속도로 15cm 후진 시키기
move('backward', 40, 15)

#endregion