"""
==========================================================
##  AWOS Finder Script  ##

Finds the AWOS or ASOS Phone number of a specified field

Christos Levy 2019
==========================================================
"""
## Import Webscrape modules
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import datetime
import os

## Contains all the different abbreviations for weather
def translator(stringOfAbbre):
    weatherStatements = []
    a = stringOfAbbre
    if "-" in a:
        weatherStatements.append("Light")
    if "+" in a:
        weatherStatements.append("Heavy")
    if "VC" in a:
        weatherStatements.append("In the Vicinity")
    if "MI" in a:
        weatherStatements.append("Shallow")
    if "PR" in a:
        weatherStatements.append("Partial")
    if "BC" in a:
        weatherStatements.append("Patches")
    if "DR" in a:
        weatherStatements.append("Low Drifting")
    if "BL" in a:
        weatherStatements.append("Blowing")
    if "SH" in a:
        weatherStatements.append("Showers")
    if "TS" in a:
        weatherStatements.append("Thunderstorm")
    if "FZ" in a:
        weatherStatements.append("Freezing")
    if "DZ" in a:
        weatherStatements.append("Drizzle")
    if "RA" in a:
        weatherStatements.append("Rain")
    if "SN" in a:
        weatherStatements.append("Snow")
    if "SG" in a:
        weatherStatements.append("Snow Grains")
    if "IC" in a:
        weatherStatements.append("Ice Crystals")
    if "PL" in a:
        weatherStatements.append("Ice Pellets")
    if "GR" in a:
        weatherStatements.append("Hail")
    if "GS" in a:
        weatherStatements.append("Small Hail/Snow Pellets")
    if "UP" in a:
        weatherStatements.append("Unknown Precipitation")
    if "BR" in a:
        weatherStatements.append("Mist")
    if "FG" in a:
        weatherStatements.append("Fog")
    if "FU" in a:
        weatherStatements.append("Smoke")
    if "VA" in a:
        weatherStatements.append("Volcanic Ash")
    if "DU" in a:
        weatherStatements.append("Widespread Dust")
    if "SA" in a:
        weatherStatements.append("Sand")
    if "HZ" in a:
        weatherStatements.append("Haze")
    if "PY" in a:
        weatherStatements.append("Spray")
    if "PO" in a:
        weatherStatements.append("Sand Whirls")
    if "SQ" in a:
        weatherStatements.append("Squalls")
    if "FC" in a:
        weatherStatements.append("Funnel Cloud")
    if "SS" in a:
        weatherStatements.append("Sandstorm")
    if "DS" in a:
        weatherStatements.append("Duststorm")

    return weatherStatements

## Contains all the different abbreviations for sky conditions
def skyTranslator(stringofSkyCond):
    s = stringofSkyCond
    skyCond = []
    if "NCD" in s:
        skyCond.append("Nil Clouds Detected")
        skyCond.append(int(s[3:len(s)])*100)
    if "CLR" in s:
        skyCond.append("Clear Skies")
        skyCond.append(int(s[3:len(s)])*100)
    if "FEW" in s:
        skyCond.append("Few Clouds")
        skyCond.append(int(s[3:len(s)])*100)
    if "SCT" in s:
        skyCond.append("Scattered Clouds")
        skyCond.append(int(s[3:len(s)])*100)
    if "BKN" in s:
        skyCond.append("Broken Clouds")
        skyCond.append(int(s[3:len(s)])*100)
    if "OVC" in s:
        skyCond.append("Overcast")
        skyCond.append(int(s[3:len(s)])*100)
    if "VV" in s:
        skyCond.append("Vertical Visibilty")
        skyCond.append(int(s[3:len(s)])*100)
    return skyCond

## Finds the AWOS of the entered airport and prints frequency and phone number
def awos(airportID):
    html = urlopen("http://airnav.com/airport/"+airportID) #Opens URL and converts to HTML
    airNav = bs(html,features="html.parser") # Converts to a soup file
    f = open("Webdata.txt",'w+') # Opens a file to place webdata

    ## Loop finds all table instances in HTML and writes them to the file
    for strings in airNav.find_all('td'): 
        f.write(strings.get_text())
    f.close()

    ## Searches table HTML content for AWOS or ASOS
    with open('Webdata.txt','r') as f:
        for line in f:
            line.rstrip('\n')
            if "ASOS" in line or "AWOS" in line:
                return line
                directory = os.getcwd()+'/Webdata.txt'
                os.remove(directory)
                break
    

def metar(airportID):
    ## Checks if airport has a metar
    for a in list(airportID):
        try:
            a = int(a)
            return("Airport does not have a METAR.\n")
            break
        except:
            continue

    ## Opens Webpage
    html = urlopen("http://aviationweather.gov/metar/data?ids="+airportID+"&format=raw&date=&hours=0")
    metarPage = bs(html,features="html.parser")
    
    ## Creates a list of every metar attribute
    for metarLine in metarPage.find_all('code'):
        fullMetar = metarLine.get_text()
    metar = fullMetar.split()

    ## Removes unnecessary info
    for i in metar:
        if i == 'RMK':
            for j in range(len(metar)-1,metar.index(i),-1):
                del metar[j]
            metar.remove(i)
        if i == "AUTO":
            metar.remove(i)
    
    ## Constants
    airport = metar[0]

    ## TIME VALUES (DATE AND ZULU TIME)
    dt = datetime.datetime.today()
    time = metar[1]
    date = f"{dt.month}/{int(time[0:2])}/{dt.year}"
    zuluTime = f"{time[2:6]} Zulu"

    ## WIND VALUES (direction,velocity,gust(try))
    wind = metar[2]
    if "VRB" in wind:
        visibility = metar[3]
        velocity = f"{wind[3:5]} knots"
        if "G" in wind:
            gust = f" Gusting {wind[6:8]} knots"
        direction = "Variable Direction"
    if "V" in metar[3]:
        variation = metar[3]
        visibility = metar[4]
        direction = f"Wind Variable between {variation[0:2]} and {variation[3:6]}"
    else:
        direction = f"{wind[0:3]} Degrees"
        velocity = f"{wind[3:5]} knots"
        visibility = metar[3]
        if "G" in wind:
            gust = f"Gusting {wind[6:8]} knots"
    

    # VISIBILITY VALUES(visibiltyNum)
    if "SM" not in visibility:
        addOn = float(visibility)
        visibility = metar[metar.index(visibility)+1]
    else:
        addOn = 0

    if "/" in visibility:
        frac = True
    else:
        frac = False
    visibilityNumList = visibility.split("SM")

    if frac == True:
        fracList = visibilityNumList[0].split("/")
        num = float(fracList[0])/float(fracList[1])
        visibilityNum = f"{num+addOn} Statute Miles"
    try:
        visibilityNum = f"{float(visibilityNumList[0])+addOn} Statute Mile(s)"
    except:
        if "M" in visibility:
            visibilityNum = f"Less than 1/4 Statute Miles"
        if "P" in visibility:
            visibilityNum = f"Greater than 10 Statute Miles"


    ## WEATHER CHECKER (weather and sky conditions)
    listofSkyConds = []
    if len(metar[metar.index(visibility)+1]) < 6 or len(metar[metar.index(visibility)+1]) > 6:
        weather = metar[metar.index(visibility)+1] ## Statement is made for both cases of visibility (being index 3 or 4)
        weather = translator(weather)
        counter = metar.index(weather)+1
    else:
        weather = "No Weather"
        listofSkyConds.append(metar[metar.index(visibility)+1])
        counter = metar.index(visibility)+2
        
    
    
    
    while True:
        if not("/" in metar[counter]):
            listofSkyConds.append(metar[counter])
            counter+=1
        else:
            break
    skyCond = []

    ## Translates SkyConds:
    for i in listofSkyConds:
        skyCond.append(skyTranslator(i))

    ## Temperature
    tempDew = metar[counter]
    tempDew = tempDew.split("/")
    for t in range(len(tempDew)):
        if "M" in tempDew[t]:
            tempDew[t] = -int(tempDew[t][1:len(tempDew[t])])
        else: 
            tempDew[t] = tempDew[t]
    tempDew = f"Temperature: {int(tempDew[0])} Degrees Celsius\nDew Point: {int(tempDew[1])} Degrees Celsius"

    ## Altimeter
    altimeter = metar[counter+1]
    altimeter = altimeter[1:len(altimeter)]
    altimeter = f"Altimeter: {altimeter[0:2]}.{altimeter[2:len(altimeter)]}"


    ## Format Variables into strings
    html = urlopen("http://airnav.com/airport/"+airportID) #Opens URL and converts to HTML
    airNav = bs(html,features="html.parser") # Converts to a soup file
    airportName = airNav.title.string
    airportName = airportName[8:len(airportName)]
    
    try:
        return(f"\nFull Metar: {fullMetar}\n{airportName}\n{date}\n{zuluTime}\nWind: {direction} at {velocity}, {gust}\nVisibility: {visibility}\n{weather}\n{skyCond}\n{tempDew}\n{altimeter}")
    except:
        return(f"\nFull Metar: {fullMetar}\n{airportName}\n{date}\n{zuluTime}\nWind: {direction} at {velocity}\nVisibility: {visibility}\n{weather}\n{skyCond}\n{tempDew}\n{altimeter}")
    


### ALL FUNCTIONS TESTED AND COMPLETED FOR AWOS CLASS


