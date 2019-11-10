#/usr/bin/python3
"""
==========================================================
##  Watch Class  ##

Contains several time related functions

Christos Levy 2019
==========================================================
"""

import time


## This function prints a stopwatch on the screen
def stopwatch():
    print("STOPWATCH FUNCTION\nType Control-C to end")
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
                Sec+=1
                print(f"{Min} Minute(s) {Sec} Second(s)", end = '\r')
                time.sleep(1)
                
                if Sec == 60:
                    Sec = 0
                    Min += 1
                if Min > 60:
                    Hour += 1
            elif Hour > 0:
                Sec += 1
                print(f"{Hour} Hour(s) {Min} Minute(s) {Sec} second(s)", end = "\r")
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
                print(f"{min} Minute(s) {sec} Second(s)" , end = "\r")
                time.sleep(1)

            elif sec == 0:
                min-=1
                sec = 60
                print(f"{min} Minute(s) {sec} Second(s)", end = "\r")
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

## This function converts degrees celsius to fahrenheit and vice versa
def tempConvert(type,degrees):
    if type == "1": ##Convert to celsius
        celsius = (5/9)*(degrees-32)
        return f"{round(celsius,1)} Degrees Celsius"
    elif type == "2": ## Convert to farenheit
        faren = (9/5)*degrees + 32
        return f"{round(faren,1)} Degrees Fahrenheit"
    else:
        return


### ALL FUNCTIONS TESTED AND COMPLETED FOR WATCH CLASS