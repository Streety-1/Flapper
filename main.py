# /flappernought/FlapperUpdater.py
# /flappernought/Flapper

#------------------------------------IMPORTS------------------------------------#
import os
import subprocess
import time
import datetime
import curses
import RPi.GPIO as GPIO
import socket
#------------------------------------VALUES------------------------------------#
timenow = datetime.datetime.now()

b = '\033[1;34;40m'

last_press_time = 0
debounce_delay = 0.5  # 500 milliseconds

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def run_python(name):
    systemCmd("clear")
    exec(open(name).read())

#------------------------------------Buttons------------------------------------#
GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
#------------------------------------START------------------------------------#

def update():
    print("run update")
    #run FlapperUpdater.py again

def shutdown():
    systemCmd('sudo shutdown -h now')

def ap_scan():
    systemCmd("clear")
    time.sleep(2)
    run_python('ap-scanner.py')

def main(stdscr):
    systemCmd("clear")

    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking
    stdscr.timeout(100) # Refresh screen every 100 milliseconds
    curses.start_color()
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_YELLOW)

    # Custom text to display at the top
    top_text = """
+ select
- navigate
  ___  _                             
 | __|| | __ _  _ __  _ __  ___  _ _ 
 | _| | |/ _` || '_ \| '_ \/ -_)| '_|
 |_|  |_|\__,_|| .__/| .__/\___||_|  
               |_|   |_|                                       
    """

    # List of menu options with associated color pairs
    menu = [
        ("Update"),
        ("Shutdown")
    ]
    current_row = 0

    h, w = stdscr.getmaxyx()

    while True:
        global last_press_time
        current_time = time.time()

        # Display the custom top text
        stdscr.addstr(0, 0, top_text, curses.A_BOLD | curses.color_pair(4))

        # Display the menu
        for idx, (text) in enumerate(menu):
            x = 4
            y = h // 2 - len(menu) // 2 + idx - 2
            if idx == current_row: #selected
                stdscr.addstr(y, x, text, curses.A_BOLD | curses.color_pair(3))
            else: #not selected
                stdscr.addstr(y, x, text, curses.A_BOLD | curses.color_pair(4))

        stdscr.refresh()

        # Navigate the menu
        if not GPIO.input(23): # top button click SELECT
            if current_time - last_press_time >= debounce_delay:
                last_press_time = current_time

                # Select option
                selection = menu[current_row][0]
                print(selection)

                if 'U' in selection:
                    update()
                elif 'S' in selection:
                    shutdown()


        if not GPIO.input(24): #navigate menu
            if current_time - last_press_time >= debounce_delay:
                last_press_time = current_time
                current_row = (current_row + 1) % len(menu)

        time.sleep(0.1)  # Small delay to prevent high CPU usage



#Start Main menu
curses.wrapper(main)