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
    return m.asin(m.radians(x))
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
    wca = (180/m.pi)*( m.asin( (wspd*sin(wdir-crs)) /gs ) )
    heading = round(crs + wca)
    print(f"GROUNDSPEED: {gs}\nHEADING: {heading}\nWCA: {wca}")

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
    print(f"PRESSURE ALTITUDE: {pAlt}\nDENSITY ALTITUDE: {dAlt}")

pressureDensityAlt()