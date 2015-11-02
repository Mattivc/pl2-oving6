from robot import motors
from time import sleep

mot = motors.Motors()

duration = 0.25
speed = 0.8

while True:

    move = input('Input: ')

    for c in move:
        if c == 'w':
            mot.forward(speed, duration)
        elif c == 's':
            mot.backward(speed, duration)
        elif c == 'a':
            mot.left(speed, duration)
        elif c == 'd':
            mot.right(speed, duration)
        sleep(duration*1.2)
