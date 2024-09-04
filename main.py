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
    
#------------------------------------START------------------------------------#

def ap_scan():
    print("Running...")
    time.sleep(3)
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
    print('\n')
    print(b + """
  _   _                   _     _   
 | \ | |                 | |   | |  
 |  \| | ___  _   _  __ _| |__ | |_ 
 | . ` |/ _ \| | | |/ _` | '_ \| __|
 | |\  | (_) | |_| | (_| | | | | |_ 
 |_| \_|\___/ \__,_|\__, |_| |_|\__|
                     __/ |          
                    |___/                                            
       """)
    print('\n'*2)

    print(b+'Please select an option: ')

    time.sleep(60)





    #Menu

main_menu()
