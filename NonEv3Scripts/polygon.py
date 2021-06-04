from time import sleep
import turtle
t = turtle.Pen()
sides = int(input('How many sides?'))
for n in range(sides):
    t.forward(100)
    t.left(360/sides)
sleep(1)