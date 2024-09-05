# /flappernought/FlapperUpdater.py
# /flappernought/Flapper

#------------------------------------IMPORTS------------------------------------#
import os
import time
import datetime

#------------------------------------VALUES------------------------------------#
timenow = datetime.datetime.now()

b = '\033[1;34;40m'

#-------------------Functions-------------------#

def systemCmd(command):
    os.system(command)

def run_python(name):
    systemCmd("clear")
    exec(open(name).read())

systemCmd('sudo apt install python3-InquirerPy')

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy import inquirer

#------------------------------------START------------------------------------#

def update():
    checkupd = inquirer.confirm(message="This will install the latest build.").execute()

    if checkupd:
        systemCmd("cd /")
        systemCmd("sudo python3 flappernought/FlapperUpdater.py")
    if not checkupd:
        main_menu()

def ap_scan():
    systemCmd("clear")
    time.sleep(2)
    run_python('ap-scanner.py')

def main_menu():
    systemCmd("clear")
    print(b+"""
  ___  _                             
 | __|| | __ _  _ __  _ __  ___  _ _ 
 | _| | |/ _` || '_ \| '_ \/ -_)| '_|
 |_|  |_|\__,_|| .__/| .__/\___||_|  
               |_|   |_|                                       
    """)

    Selection = inquirer.select(
        message="Please select an option:",
        choices=[
            "AP scanner",
            "Update"
        ],
        default=None,
    ).execute()
    selected = Selection
    
    print(b+'Please select an option: ')

    if selected == "Update":
        update()
    if selected == "AP scanner":
        ap_scan()


main_menu()
