'''
===============================================================================
ENGR 133 Program Description 
	Flight script containing functions related to inflight calculations

Project Information
	Project Title:  Lev6B
	Author:         Christos Levy, levy30@purdue.edu
	Team ID:        002-10
===============================================================================
'''

## Takes time and ground speed and returns the distance flown
def distFln(gs,hr,min,sec):
    minToH = min/60
    secToH = sec/3600
    totalHours = minToH + secToH + hr
    dist = round(gs*totalHours,1)
    return f"{dist} Mile(s)"

## Returns the distance that is the top of the descent
def topDscn(gs,ialt,dalt,rate):
    alt = ialt-dalt ## Altitude to descend
    if rate == 0:
        return 0
    else:
        timeM = alt/rate ## Time in minutes
        timeH = timeM/60
        dist = round(timeH*gs,1)
        return f"{dist} Mile(s)"

## Returns the Endurance of the Aircraft based on the amount of fuel it contains and its fuel burn
def endur(fuel,fph):
    if fph == 0:
        return 0
    else:
        hours = fuel/fph
        if hours % 1 == 0:
            return f"{hours} Hour(s)"
        else:
            remainderM = hours % 1
            minutes = 60*remainderM
            remainderS = minutes%1
            seconds = int(remainderS*60)
            return f"{int(hours)} Hour(s) {int(minutes)} minute(s) {seconds} second(s)"

## Returns the time the leg will take given the ground speed and the distance
def legTime(distance,gs):
    if gs == 0:
        return 0 
    else:
        time = distance/gs
        if time%1 == 0:
            return f"{time} Hours"
        else:
            remM = time%1
            hours = int(time)
            min = (remM*60)
            sec = (min%1)*60
            sec = int(sec)
            return f"{hours} Hour(s) {int(min)} Minute(s) {sec} Second(s)"

## Calulates the Range at altitude given the amount of fuel, the fuel burn, and the ground speed
def spcRange(fuel,fph,gs):
    if fph == 0:
        return 0
    else:
        time = fuel/fph
        range = round(time*gs,1)
        return f"{range} Mile(s)"

## Calculates the fuel burn given the time and the amount of fuel burned
def fuelPerHour(fuel,hour,min,sec):
    minToH = min/60
    secToH = sec/3600
    time = hour+minToH+secToH
    if time == 0:
        return 0
    else:
        fph = fuel/time
        return f"{round(fph,1)} Gallons per Hour"




### ALL FUNCTIONS TESTED AND COMPLETED FOR FLIGHT CLASS