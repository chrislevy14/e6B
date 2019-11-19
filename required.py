"""
==========================================================
##  Required Functions Class  ##

Contains functions of required operations

Christos Levy 2019
==========================================================
"""

import math as m
def cos(x):
    return m.cos(m.radians(x))
def sin(x):
    return m.sin(m.radians(x))
def asin(x):
    return m.degrees(m.asin(x))

## Returns the required amount of fuel necessary for a given time and fuel burn
def fuel():
    while True:
        hours = input("Enter hours: ")
        minutes = input("Enter minutes: ")
        seconds = input("Enter seconds: ")
        fph = input("Enter Fuel burn: ")
        try:
            hours = float(hours)
            minutes = float(minutes)
            seconds = float(seconds)
            fph = float(fph)
            break
        except:
            print("Error: All values must be numbers\n")
            continue
    mintoH = minutes/60
    sectoH = seconds/3600
    hours += mintoH + sectoH
    fuel = round(fph*hours,1)
    return f"\nRequired Fuel: {fuel} Gallons"

## Returns the required rate of climb given the minimum climb and the groundspeed
def climb():
    while True:
        minClimb = input("Enter Minimum climb in feet per mile: ")
        groundspeed = input("Enter groundspeed: ")
        try:
            minClimb = float(minClimb)
            groundspeed = float(groundspeed)
            break
        except:
            print("Error: All values must be numbers\n")
            continue 
    requiredClimb = round((minClimb*groundspeed)/60,1)
    return f"\nRequired Rate of Climb: {requiredClimb} Feet Per Minute"

## Returns the rate of descent 
def descent():
    while True:
        ialt = input("Enter Indicated Altitude: ")
        destAlt = input("Enter Crossing Altitude: ")
        groundspeed = input("Enter Groundspeed: ")
        fixDist = input("Enter Fix Distance: ")
        try:
            ialt = float(ialt)
            destAlt = float(destAlt)
            groundspeed = float(groundspeed)
            if groundspeed == 0:
                return 0
            fixDist = float(fixDist)
            break
        except:
            print("Error: All values must be numbers\n")
            continue 
    diffAlt = ialt-destAlt
    if groundspeed == 0:
        return 0
    time = fixDist/groundspeed
    minutes = time*60
    if minutes == 0:
        return 0
    descentRate = int(round(diffAlt/minutes,-1))
    return f"\nRequired Rate of Descent: {descentRate} Feet Per Minute"

## Returns true airspeed given wind direction, wind speed, course and grounspeed
def tas():
    while True:
        wdir = input("Enter Wind Direction: ")
        wspd = input("Enter Wind Speed: ")
        course = input("Enter Course: ")
        groundspeed = input("Enter Groundspeed: ")
        try:
            wdir,wspd,course,groundspeed = float(wdir),float(wspd),float(course),float(groundspeed)
            break
        except:
            print("Error: Values must be numbers\n")
            continue
    angleB = abs(wdir-course)
    if groundspeed == 0:
        return 0
    angleC = asin((sin(angleB)*wspd)/(groundspeed))
    angleA = 180-angleB-angleC
    tas = round(m.sqrt(groundspeed**2+wspd**2-(2*(groundspeed)*(wspd)*cos(angleA))),1)
    hdg = int(round(course+angleC,0))
    return f"TAS: {tas}\nHeading: {hdg}\n"


### ALL FUNCTIONS TESTED AND COMPLETED FOR REQUIRED CLASS







