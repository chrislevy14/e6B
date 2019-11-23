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



