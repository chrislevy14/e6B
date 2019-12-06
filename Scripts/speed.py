'''
===============================================================================
ENGR 133 Program Description 
	Speed script containing speed related functions

Project Information
	Project Title:  Lev6B
	Author:         Christos Levy, levy30@purdue.edu
	Team ID:        002-10
===============================================================================
'''

import math as m

## Returns the ground speed given the time and the distance
def gs():
    while True:
        distance = input("Enter Distance covered: ")
        hours = input("Enter Hours: ")
        minutes = input("Enter Minutes: ")
        seconds = input("Enter Seconds: ")
        try:
            distance = float(distance)
            hours = float(hours)
            minutes = float(minutes)
            seconds = float(seconds)
            break
        except:
            print("Error: Values must be numbers\n")
            continue
    secToH = seconds/3600
    minToH = minutes/60
    hours += secToH + minToH
    if hours == 0:
        return 0
    else:
        groundspeed = round(distance/hours,1)
        return f"\nGroundspeed: {groundspeed} MPH"

## Returns True airpseed given the pressure altitude and indicated airspeed
def planTAS():
    while True:
        indicatedAS = input("Enter Indicated Airspeed: ")
        altitdue = input("Enter Altitude: ")
        try:
            indicatedAS,altitdue = float(indicatedAS),float(altitdue)
            break
        except:
            print("Error: All values must be numbers")
            continue
    TrueAS = round(indicatedAS + (.02*altitdue/1000),1)
    return f"\nTrue Airspeed: {TrueAS}\n"

## Returns the true airpseed based on the pressure altitude and the outside temperature. Uses the NOAA equation for pressure and various constants
def actTAS():
    while True:
        pressureAlt = input("Enter Pressure Altitdue: ")
        temp = input("Enter Temperature in Celsius: ")
        ias = input("Enter indicated airpseed: ")
        try:
            pressureAlt,temp,ias = float(pressureAlt),float(temp),float(ias)
            break
        except:
            print("Error: Numbers must be numeric.\n")
            continue
    tempK = 273.15+temp
    if tempK == 0:
        return 0
    dalt = round(pressureAlt + 120*(temp-(15-(pressureAlt/1000)*2)),1)
    pressureinPascals = 100*(m.exp(m.log(1-(pressureAlt/145366.45))/0.190284)*1013.25)
    density = pressureinPascals/(287.058*tempK)
    if density == 0:
        return 0
    tas = round(ias*m.sqrt(1.225/density),1)
    return f"\nTAS: {tas}\nDenstiy Altitude: {dalt}\n"



### ALL FUNCTIONS TESTED AND COMPLETED FOR SPEED CLASS

