from robot import motors
from time import sleep

mot = motors.Motors()

duration = 0.25
speed = 1.0

while True:

    move = input('Input: ')
    if move == 'w':
        mot.forward(speed, duration)
    elif move == 's':
        mot.backward(speed, duration)
    elif move == 'a':
        mot.left(speed, duration)
    elif move == 'd':
        mot.right(speed, duration)
    sleep(duration)
