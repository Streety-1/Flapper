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
    # Initialize curses
    curses.curs_set(1)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking
    stdscr.timeout(100) # Refresh screen every 100 milliseconds

    curses.start_color()
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Custom text to display at the top
    top_text = """
  ___  _                             
 | __|| | __ _  _ __  _ __  ___  _ _ 
 | _| | |/ _` || '_ \| '_ \/ -_)| '_|
 |_|  |_|\__,_|| .__/| .__/\___||_|  
               |_|   |_|                                       
    """

    # List of menu options with associated color pairs
    menu = [
        ("AP scanner", 4),
        ("Update", 4),
        ("Shutdown", 4)
    ]
    current_row = 0

    h, w = stdscr.getmaxyx()

    margin = 5
    v_offset = 3

    while True:
        # Display the custom top text
        stdscr.addstr(0, 0, top_text, curses.A_BOLD | curses.color_pair(4))

        # Display the menu
        for idx, (text, color_pair) in enumerate(menu):
           # x = w // 2 - len(text) // 2
            x = 5
            y = h // 2 - len(menu) // 2 + idx - 3
            if idx == current_row:
                stdscr.attron(curses.color_pair(color_pair) | curses.A_REVERSE)
                stdscr.addstr(y, x, text)
                stdscr.attroff(curses.color_pair(color_pair) | curses.A_REVERSE)
            else:
                stdscr.attron(curses.color_pair(color_pair))
                stdscr.addstr(y, x, text)
                stdscr.attroff(curses.color_pair(color_pair))

        stdscr.refresh()

        key = stdscr.getch()

        # Navigate the menu
        if key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(menu)
        elif key == curses.KEY_UP:
            current_row = (current_row - 1) % len(menu)
        elif key == ord('\n'):  # Enter key
            stdscr.addstr(h // 2 + len(menu), w // 2 - len(f"You selected '{menu[current_row][0]}'") // 2, f"You selected '{menu[current_row][0]}'")
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
