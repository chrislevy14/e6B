
"""
==========================================================
##  Watch Class  ##

Contains several time related functions

Christos Levy 2019
==========================================================
"""

import time
import sys
#import keyboard


## This function prints a stopwatch on the screen
def stopwatch():
    print("TIMER FUNCTION\n")
    ## Get Start Input
    timeLoop = False
    while True:
        start = input("Would you like to begin Timing? (y/n): ").lower()
        if start == "y":
            timeLoop = True
            break
        elif start == "n":
            break
        else:
            print("Error: Enter (Y/N)\n")

    ## Initiate Variables at 0
    Sec = 0
    Min = 0
    Hour = 0

    ## Begin timeLoop that prints time
    while timeLoop:
        try:
            if Hour == 0:
                Sec += 1
                print(f"{Min} Minute(s) {Sec} second(s)", end = '\r')
                time.sleep(1)
                if Sec == 60:
                    Sec = 0
                    Min += 1
                if Min > 60:
                    Hour += 1
            elif Hour > 0:
                Sec += 1
                print(f"{Hour} Hour(s) {Min} Minute(s) {Sec} second(s)" , end = '\r')
                time.sleep(1)
                if Sec == 60:
                    Sec = 0
                    Min += 1
                if Min > 60:
                    Hour += 1
        except KeyboardInterrupt: ## Need a better way to kill the program. 
            timeLoop = False
            break
    
## This function Counts down like a timer
def timer(hour,min,sec):
    timerDone = False

    ## Converts hours to minutes to make the code less complex
    min += hour*60
    while True:
        try:
            if sec > 0:
                sec -= 1
                print(f"{min} Minute(s) {sec} Second(s)" , end = '\r')
                time.sleep(1)
            elif sec == 0:
                min-=1
                sec = 60
                print(f"{min} Minute(s) {sec} Second(s)", end = '\r')
                time.sleep(1)
            if sec == 0 and min == 0:
                timerDone = True
                break
        except KeyboardInterrupt: ## Need a better way to kill the program.
            break

    while timerDone:
        try:
            print("Timer Done!")
            time.sleep(0.5)
        except KeyboardInterrupt: ## Need a better to kill program
            break



stopwatch()
