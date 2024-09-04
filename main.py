#------------------------------------IMPORTS------------------------------------#
import os
import time
import datetime

#------------------------------------VALUES------------------------------------#
clear = lambda: os.system('cls')

timenow = datetime.datetime.now()

b = '\033[1;34;40m Bright Blue'

#------------------------------------GET VERSION------------------------------------#



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
    print('\n' * 20)
    print(b+"| Flapper Nought |")
    print(timenow.strftime(b+"%m-%d %H:%M"))
    time.sleep(60)


    #Menu

main_menu()
