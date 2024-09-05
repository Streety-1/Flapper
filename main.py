# /flappernought/FlapperUpdater.py
# /flappernought/Flapper

#------------------------------------IMPORTS------------------------------------#
import os
import subprocess
import time
import datetime
import curses
import RPi.GPIO as GPIO

#------------------------------------VALUES------------------------------------#
timenow = datetime.datetime.now()

b = '\033[1;34;40m'

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def run_python(name):
    systemCmd("clear")
    exec(open(name).read())

#------------------------------------Buttons------------------------------------#
GPIO.setmode(GPIO.BCM)

# Define GPIO pins connected to the buttons
BUTTONA_PIN = 23  # Change to your button 1 GPIO pin
BUTTONB_PIN = 24  # Change to your button 2 GPIO pin

# Setup GPIO pins as input with pull-up resistors
GPIO.setup(BUTTONA_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTONB_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttona_callback(channel):
    print("Button a pressed!")

def buttonb_callback(channel):
    print("Button b pressed!")

# Add event detection for the buttons
GPIO.add_event_detect(BUTTONA_PIN, GPIO.FALLING, callback=buttona_callback, bouncetime=200)
GPIO.add_event_detect(BUTTONB_PIN, GPIO.FALLING, callback=buttonb_callback, bouncetime=200)

#------------------------------------START------------------------------------#

def update():
    print("yo")

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

    while True:
        # Display the custom top text
        stdscr.addstr(0, 0, top_text, curses.A_BOLD | curses.color_pair(4))

        # Display the menu
        for idx, (text, color_pair) in enumerate(menu):
            x = 4
            y = h // 2 - len(menu) // 2 + idx - 2
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
            selection = menu[current_row][0]


            if selection == Update:
                update()



            #stdscr.addstr(h // 2 + len(menu), w // 2 - len(f"You selected '{menu[current_row][0]}'") // 2, f"You selected '{menu[current_row][0]}'")
            stdscr.refresh()
            stdscr.getch()
        elif key == 27:  # ESC key to exit
            break
            GPIO.cleanup()

def main_menu():
    systemCmd("clear")
    curses.wrapper(main) #launch main UI

main_menu()
