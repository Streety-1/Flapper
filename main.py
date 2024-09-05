# /flappernought/FlapperUpdater.py
# /flappernought/Flapper

#------------------------------------IMPORTS------------------------------------#
import os
import subprocess
import time
import datetime
import curses

#------------------------------------VALUES------------------------------------#
timenow = datetime.datetime.now()

b = '\033[1;34;40m'

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def run_python(name):
    systemCmd("clear")
    exec(open(name).read())

#------------------------------------START------------------------------------#

#def update():

def ap_scan():
    systemCmd("clear")
    time.sleep(2)
    run_python('ap-scanner.py')

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # List of menu options
    menu = ["Option 1", "Option 2", "Option 3", "Option 4"]
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # Display the menu
        for idx, row in enumerate(menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu) // 2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()

        key = stdscr.getch()

        # Navigate the menu
        if key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(menu)
        elif key == curses.KEY_UP:
            current_row = (current_row - 1) % len(menu)
        elif key == ord('\n'):  # Enter key
            stdscr.addstr(h // 2 + len(menu), w // 2 - len("You selected '{}'".format(menu[current_row])) // 2, "You selected '{}'".format(menu[current_row]))
            stdscr.refresh()
            stdscr.getch()
        elif key == 27:  # ESC key to exit
            break

def main_menu():
    systemCmd("clear")
    print(b+"""
  ___  _                             
 | __|| | __ _  _ __  _ __  ___  _ _ 
 | _| | |/ _` || '_ \| '_ \/ -_)| '_|
 |_|  |_|\__,_|| .__/| .__/\___||_|  
               |_|   |_|                                       
    """)

    curses.wrapper(main)


main_menu()
