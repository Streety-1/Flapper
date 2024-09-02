# Download Latest version from github repo
# https://github.com/Streety-1/Flapper-Nought.git

#run updater to launch script 

import os
import subprocess
import sys
import urllib.request
import time

urltocheckwifi = "https://www.google.com/ "

requiredmodules = {'simple-term-menu'}

#-------------------Prequisit Installer-------------------#

def systemCmd(command):
    os.system(command)

def pipinstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL)

try:
    pipinstall('requests')
    import requests
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

    print("| Updating Git |")
    systemCmd('sudo apt install git --quiet')

    print("| Cloning repo for latest version |")
    #Delete existing flapper file then install new one and run main from it




except urllib.error.URLError:
    print("Error: No wifi connection")
    task.wait(5)

