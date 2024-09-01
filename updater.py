# Download Latest version from github repo
# https://github.com/Streety-1/Flapper-Nought.git

import subprocess
import sys
import urllib.request
import requests

urltocheckwifi = "https://www.google.com/"

requiredmodules = {'requests', 'simple-term-menu'}

#-------------------Prequisit Installer-------------------#

def systemCmd(command):
    os.system(command)

def pipinstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL)

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
    
    
    
    #get script from git and launch
    
    
    
    clear()

except urllib.error.URLError:
    print("No wifi")

