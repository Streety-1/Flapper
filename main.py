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
button_press_start_time = None # Variable to track when the button press started
long_hold_duration = 0.5

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def run_python(name):
    systemCmd("clear")
    exec(open(name).read())

def get_ip_address():
    # Get the local IP address of the Raspberry Pi (on the same network)
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

#------------------------------------Buttons------------------------------------#
GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)

#------------------------------------START------------------------------------#

def update():
    print("yo")

def shutdown():
    systemCmd('sudo shutdown -h now')

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

    ip_address = get_ip_address()

    piIP = commands.getoutput('hostname -I')

    # List of menu options with associated color pairs
    menu = [
        ("AP scanner", 4),
        ("Update", 4),
        ("Shutdown", 4)
    ]
    current_row = 1

    h, w = stdscr.getmaxyx()

    while True:
        global button_press_start_time
        global last_press_time
        global long_hold_duration
        current_time = time.time()

        # Display the custom top text
        stdscr.addstr(0, 0, top_text, curses.A_BOLD | curses.color_pair(4))

        #IP
        stdscr.addstr(4, 0, f"IP Address: {ip_address}", curses.A_BOLD | curses.color_pair(4))

        # Display the menu
        for idx, (text, color_pair) in enumerate(menu):
            x = 4
            y = h // 2 - len(menu) // 2 + idx - 2
            if idx == current_row:
                stdscr.attron(curses.color_pair(color_pair) | curses.A_REVERSE)
                stdscr.addstr(y, x, text, curses.A_BOLD)
                stdscr.attroff(curses.color_pair(color_pair) | curses.A_REVERSE)
            else:
                stdscr.attron(curses.color_pair(color_pair))
                stdscr.addstr(y, x, text, curses.A_BOLD)
                stdscr.attroff(curses.color_pair(color_pair))

        stdscr.refresh()

        key = stdscr.getch()

        # Navigate the menu
        if not GPIO.input(23): # top button
            if current_time - last_press_time >= debounce_delay:
                last_press_time = current_time

                # check for hold
                if button_press_start_time is None:
                    # Record the time when button is first pressed
                    button_press_start_time = time.time()
                else:
                    # Check if the button has been held long enough
                    if time.time() - button_press_start_time >= long_hold_duration:
                        # Perform the action for a long press here

                        # Select option
                        selection = menu[current_row][0]

                        if 'Update' in selection:
                            update()
                        elif 'Shutdown' in selection:
                            shutdown()

                        stdscr.refresh()
                        stdscr.getch()
                        button_press_start_time = None  # Reset the start time
        else:
            if button_press_start_time is not None:
                # The button was pressed but is now released
                press_duration = time.time() - button_press_start_time
                if press_duration < long_hold_duration:
                    # short click
                    last_press_time = current_time
                    current_row = (current_row - 1) % len(menu)
                # Reset the start time
                button_press_start_time = None

        if not GPIO.input(24): # bottom button
            if current_time - last_press_time >= debounce_delay:
                last_press_time = current_time
                current_row = (current_row + 1) % len(menu)

        time.sleep(0.1)  # Small delay to prevent high CPU usage

def main_menu():
    systemCmd("clear")
    curses.wrapper(main) # launch main UI

main_menu()
