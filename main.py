#------------------------------------IMPORTS------------------------------------#
import os
import time
from simple_term_menu import TerminalMenu

#------------------------------------VALUES------------------------------------#
clear = lambda: os.system('cls')

#------------------------------------GET VERSION------------------------------------#

with open("version.txt", "r") as file:
    ver = file.read()
    ScriptVersion = ver

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def runPython(name):
    clear()
    exec(open(name).read())
    
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
