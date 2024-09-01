#------------------------------------IMPORTS------------------------------------#
import os
import subprocess
import sys
import urllib.request
import time

#------------------------------------VALUES------------------------------------#
clear = lambda: os.system('cls')

ScriptVersion = 'V1'

urltocheckwifi = "https://www.google.com/"

requiredmodules = {'requests', 'simple-term-menu'}

#-------------------Functions-------------------#
def pipinstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL)

def systemCmd(command):
    os.system(command)

def runPython(name):
    clear()
    exec(open(name).read())

#-------------------Prequisit Installer-------------------#

try:
    urllib.request.urlopen(urltocheckwifi)
    print("| Updating pip |")
    systemCmd('python.exe -m pip install --upgrade pip --quiet')
    print("| Updating modules |")

    #install modules
    for x in requiredmodules:
        try:
            import x
            print("\033[2J\033[H", end="", flush=false)
        except ImportError:
            pipinstall(x)

    print("| Updating dbus |")
    systemCmd('sudo apt install python-dbus --quiet')
    clear()

except urllib.error.URLError:
    print("No wifi")

#------------------------------------INSTALLED IMPORTS------------------------------------#

import requests
from simple_term_menu import TerminalMenu

#------------------------------------START------------------------------------#

def Wifi():
    print("Running...")
    time.sleep(3)
    runPython('ap-scanner.py')

def CheckForUpdate():
    print("Running...")
    time.sleep(3)
    runPython('updater.py')

def MainMenu():
    clear()
    print("| Flapper Nought |")
    print(ScriptVersion)

    options = ["AP Scanner", "Update"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if options[menu_entry_index] == "AP Scanner":
        print("AP")
    if options[menu_entry_index] == "Update":
        print("Update")

    print(f"You have selected {options[menu_entry_index]}!")

MainMenu()
