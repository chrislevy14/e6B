"""
=============================================
##  Weather Class  ##

Contains weather and heading functions

Christos Levy 2019
=============================================
"""
import math as m

## Redfine Sin and cos functions for easy usage
def sin(x):
    return m.sin(m.radians(x))
def asin(x):
    return m.degrees(m.asin(x))
def cos(x):
    return m.cos(m.radians(x))


## Calculates the groundspeed, the wind correction angle and the heading
def hdgGs():
    while True:
        wdir = input("Wind Direction: ")
        wspd = input("Enter Windspeed: ")
        crs = input("Enter Course: ")
        tas = input("Enter True Airspeed: ")
        try:
            wdir = float(wdir)
            wspd = float(wspd)
            crs = float(crs)
            tas = float(tas)
            break
        except:
            print("Error: All values must be numbers\n")
            continue
    angleC = abs(wdir-crs)
    gs = round(m.sqrt(wspd**2+tas**2-(2*wspd*tas*cos(angleC))),1)
    if gs == 0:
        return 0
    else:
        wca = ( asin( (wspd*sin(wdir-crs)) /gs ) )
        heading = round(crs + wca)
        return (f"GROUNDSPEED: {gs}\nHEADING: {heading}\nWCA: {round(wca,1)}")

## Calulates the Pressure and density altitude
def pressureDensityAlt():
    while True:
        indicatedAlt = input("Enter Indicated Altitude: ")
        baro = input("Enter Barometric Pressure: ")
        temp = input("Enter Outside Temperature (Celsius): ")
        try:
            indicatedAlt = float(indicatedAlt)
            baro = float(baro)
            temp = float(temp)
            break
        except:
            print("Error: Values must be numbers\n")
    pAlt = round((29.92-baro)*1000+indicatedAlt)
    degreeChange = 15 - (-2*(indicatedAlt/1000))
    dAlt = round((temp-degreeChange)*120+pAlt)
    return (f"PRESSURE ALTITUDE: {pAlt}\nDENSITY ALTITUDE: {dAlt}")

## Returns windspeed and direction
def wind(): 
    while True:
        course = input("Enter Course: ")
        tas = input("Enter True Airspeed: ")
        groundspeed = input("Enter Groundspeed: ")
        heading = input("Enter Heading: ")
        try:
            course = float(course)
            tas = float(tas)
            groundspeed = float(groundspeed)
            heading = float(heading)
            break
        except:
            print("Error: All values must be numbers")
            continue
    windCorrAngle = heading-course
    wspd = (m.sqrt(groundspeed**2+tas**2-(2*(groundspeed)*(tas)*cos(windCorrAngle))))
    if wspd == 0:
        return 0
    else:
        angleC =asin(((groundspeed*sin(heading-course))/wspd))
        wdir = (abs(angleC+course))
        return f"\nWIND DIRECTION: {int(wdir)}\nWIND SPEED: {round(wspd,1)}"

## Returns Components of headwind and crosswind given the runway numbers and the wind
def windComponent():
    while True:
        wdir = input("Enter Wind direction: ")
        wspd = input("Enter Wind speed: ")  
        runway = input("Enter Runway number (Runway number and not heading): ")
        try:
            wdir = int(wdir)
            wspd = float(wspd)
            runway = int(runway)
            if wdir > 360:
                print("Error: Wind Direction must be less than 360")
                continue
            if runway > 36:
                print("Error: Runway must be less than 36")
                continue
            break
        except:
            print("Error: Values must be numbers")
            continue
    runwayH = runway*10
    diff = runwayH - wdir
    ang = 90-diff
    xwind = round(wspd*cos(ang),1)
    hwind = round(wspd*sin(ang),1)

    ## Multiple nested If statements determine direction
    if xwind < 0:
        xwindSide = 'Crosswind Right'
        if hwind < 0:
            hwindSide = "Tailwind"
        elif hwind > 0:
            hwindSide = "Headwind"
        else:
            hwindSide = "No Headwind Component"
    elif xwind > 0:
        xwindSide = 'Crosswind Left'
        if hwind < 0:
            hwindSide = "Tailwind"
        elif hwind > 0:
            hwindSide = "Headwind"
        else:
            hwindSide = "No Headwind Component"
    else:
        xwindSide = "No Crosswind Component"
        if hwind < 0:
            hwindSide = "Tailwind"
        elif hwind > 0:
            hwindSide = "Headwind"
        else:
            hwindSide = "No Headwind Component"
    
    return f"\n{xwindSide}: {abs(xwind)}\n{hwindSide}: {abs(hwind)}"

## Returns the cloud base in AGL and takes 1 parameter that selects which scale
def cloudBase(degreeSelect):
    while True:
        ## Fahrenheit Calculations
        if degreeSelect == 1:
            oat = input("Enter the outside temperature: ")
            dewPoint = input("Enter the dew point: ")
            try:
                oat = float(oat)
                dewPoint = float(dewPoint)
                CloudBase = ((oat-dewPoint)/4.4)*1000
                break
            except:
                print("Error: Temperatures must be numbers")
                continue
        
        ## Celsius Calculations
        elif degreeSelect == 2:
            oat = input("Enter the outside temperature: ")
            dewPoint = input("Enter the dew point: ")
            try:
                oat = float(oat)
                dewPoint = float(dewPoint)
                CloudBase = ((oat-dewPoint)/2.5)*1000
                break
            except:
                print("Error: Temperatures must be numbers")
                continue
        else:
            print("Error: Selection not recognized.")
            continue

    return f"\nCloud Base: {round(CloudBase,1)} feet AGL"
    

### ALL FUNCTIONS TESTED AND COMPLETED FOR WEATHER CLASS
