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
from fractions import Fraction

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
    if "CLR" in s:
        skyCond.append("Clear Skies")
    if "FEW" in s:
        skyCond.append("Few Clouds")
    if "SCT" in s:
        skyCond.append("Scattered Clouds")
    if "BKN" in s:
        skyCond.append("Broken Clouds")
    if "OVC" in s:
        skyCond.append("Overcast")
    if "VV" in s:
        skyCond.append("Vertical Visibilty")
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
                break


def metar(airportID):
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
    time = metar[1]
    date = int(time[0:2])
    zuluTime = time[2:6]

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
        direction = f"{wind[0:3]}"
        velocity = f"{wind[0:3]} knots"
        visibility = metar[3]
        if "G" in wind:
            gust = f" Gusting {wind[6:8]} knots"
    

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

    

    ## WEATHER CHECKER (skyCond,weth)
    weather = metar[metar.index(visibility)+1] ## Statement is made for both cases of visibility (being index 3 or 4)

    ## Checks if there are two weather statements (Sky Conditon and weather)
    if len(metar[metar.index(visibility)+2].split("/")) == 2:
        tempDew = metar[metar.index(visibility)+2]
        skyCond = weather
    else:
        skyCond = metar[metar.index(visibility)+2]
        tempDew = metar[metar.index(visibility)+3]
    
    w = translator(weather)
    s = skyTranslator(skyCond)


    ############# FINSIHED CREATING LISTS AND NOW NEEDS FORMATTING FOR WEATHER SECTION


    altimeter = metar[metar.index(tempDew)+1]
    print(s)

metar('kvll')






