#!/usr/bin/env python3
from time import sleep 
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.motor import SpeedRPS, SpeedRPM, SpeedDPS, SpeedDPM
from ev3dev2.sound import Sound

spkr = Sound()
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

spkr.speak('Rotate')

# # (pivot turn) 왼쪽으로 90도 회전시키기
# # on_for_degrees(left_speed, right_speed, degrees, brake=True, block=True) 
# spkr.speak('Turn to the left 45 degrees')
# tank_drive.on_for_degrees(0, 30, 45) 

# spkr.speak('Turn to the left 45 degrees')
# tank_drive.on_for_degrees(0, 30, 45) 

# spkr.speak('Turn to the left 90 degrees')
# tank_drive.on_for_degrees(0, 30, 90) 

# spkr.speak('Turn to the left 180 degrees')
# tank_drive.on_for_degrees(0, 30, 180) 

# spkr.speak('Turn to the right 360 degrees')
# tank_drive.on_for_degrees(30, 0, 360) 

# # 원하는 방향으로 회전시키기
# rotationDirection = 'left'      # 'right'
# rotationSpeed = 30              # 60
# rotationDegrees = 90            # 45, 180

# if rotationDirection == 'left':
#     tank_drive.on_for_degrees(0, rotationSpeed, degrees = rotationDegrees)   # 360도 = 17.58cm, 1cm = 20.47도
# elif rotationDirection == 'right':
#     tank_drive.on_for_degrees(rotationSpeed, 0, degrees = rotationDegrees)

#region rotate_pivot( ) 함수 만들기
# def rotate_pivot(direction, speed, degrees):
#     msg = 'Turn to the {0} {1} degrees'.format(direction, degrees)
#     spkr.speak(msg)
#     if direction == 'left':
#         tank_drive.on_for_degrees(0, speed, degrees = degrees * 4.286)   # 360도 = 17.58cm, 1cm = 20.47도
#     elif direction == 'right':
#         tank_drive.on_for_degrees(speed, 0, degrees = degrees * 4.286)

# # 왼쪽으로 45도 회전 시키기, 속도 30
# rotate_pivot('left', 30, 45)

# # 왼쪽으로 45도 회전 시키기, 속도 30
# rotate_pivot('left', 30, 45)

# # 왼쪽으로 45도 회전 시키기, 속도 30
# rotate_pivot('left', 30, 45)

# # 왼쪽으로 45도 회전 시키기, 속도 30
# rotate_pivot('left', 30, 45)

# # 왼쪽으로 90도 회전 시키기, 속도 30
# rotate_pivot('left', 30, 90)

# # 오른쪽으로 270도 회전 시키기, 속도 60
# rotate_pivot('right', 60, 270)
#endregion

#region rotate_spinTurn( ) 함수 만들기
def rotate_spinTurn(direction, speed, degrees):
    msg = 'Turn to the {0} {1} degrees'.format(direction, degrees)
    spkr.speak(msg)
    if direction == 'left':
        tank_drive.on_for_degrees(-speed, speed, degrees = degrees * 2.114)   # 360도 = 17.58cm, 1cm = 20.47도
    elif direction == 'right':
        tank_drive.on_for_degrees(speed, -speed, degrees = degrees * 2.114)

# 왼쪽으로 45도 회전 시키기, 속도 30
rotate_spinTurn('left', 30, 45)

# 왼쪽으로 45도 회전 시키기, 속도 30
rotate_spinTurn('left', 30, 45)

# 왼쪽으로 45도 회전 시키기, 속도 30
rotate_spinTurn('left', 30, 45)

# 왼쪽으로 45도 회전 시키기, 속도 30
rotate_spinTurn('left', 30, 45)

# 왼쪽으로 90도 회전 시키기, 속도 30
rotate_spinTurn('left', 30, 90)

# 오른쪽으로 270도 회전 시키기, 속도 60
rotate_spinTurn('right', 60, 270)
#endregion


