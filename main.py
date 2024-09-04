#------------------------------------IMPORTS------------------------------------#
import os
import time

#------------------------------------VALUES------------------------------------#
clear = lambda: os.system('cls')

#------------------------------------GET VERSION------------------------------------#

with open("version.txt", "r") as file:
    ver = file.read()
    ScriptVersion = ver

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def run_python(name):
    clear()
    exec(open(name).read())
    
#------------------------------------START------------------------------------#

def ap_scan():
    print("Running...")
    time.sleep(3)
    run_python('ap-scanner.py')

def main_menu():
    clear()
    print("| Flapper Nought |")
    print(ScriptVersion)

    #Menu

main_menu()
