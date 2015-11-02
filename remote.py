from robot import motors
from time import sleep

mot = motors.Motors()

duration = 0.1
speed = 0.8


import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

while True:

    key = stdscr.getch()

    if key == curses.KEY_UP:
        mot.forward(speed, duration)
    elif key == curses.KEY_DOWN:
        mot.backward(speed, duration)
    elif key == curses.KEY_LEFT:
        mot.left(speed, duration)
    elif key == curses.KEY_RIGHT:
        mot.right(speed, duration)
    sleep(duration*1.2)

curses.endwin()