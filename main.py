"""
=========================
##  Main Script  ##

Runs e6B Functions

Christos Levy 2019
=========================
"""

import watch as w
import flight as f
import weightBalance as wb
import weather as wthr

numError = "Error: Input(s) must be a number"

## Main Loop
while True:
    killed = False
    funKill = False
    print("\n\nWelcome to the Lev6B!")
    print("Functions are selected by typing the number. Type 'quit' to exit\n")

    while True: ## Finds Function Group
        print("Select a function group: ")
        funcGroup = "1. Weather and Heading Functions\n2. Speed Functions\n3. Required Functions\n4. Flight Functions\n5. Weight and Balance Functions\n6. Conversion and Clock Functions\n\n"
        funcGSelect = input(funcGroup)
        if funcGSelect == "quit":
            print("Thank you for using the Lev6B!")
            killed = True
            break
        try: 
            funcGSelect = int(funcGSelect)
            if funcGSelect > 6 or funcGSelect < 1:
                print("Function Group Not Recognized\n")
                continue
            else:
                break
        except:
            print("\nError: Enter the number of the list or type 'quit' to exit")
            continue
  
    if killed == True: ## Kills the entire Program
        break

    while killed == False:
        while True:

            ## Weather and Heading Functions
            if funcGSelect == 1:
                a = 1

            ## Speed Functions
            elif funcGSelect == 2:
                a = 2

            ## Required Functions
            elif funcGSelect == 3:
                a = 3
            
            ## Flight Functions WORKING
            elif funcGSelect == 4: 
                while funKill == False:
                    funcSelect = input("\n1. Distance Flown\n2. Top of Descent\n3. Endurance\n4. Leg Time\n5. Specific Range\n6. Fuel Per Hour\n7. Quit to Main Menu\n")
                    try:
                        funcSelect = int(funcSelect)
                    except:
                        print(f"{numError}\n")
                        continue
                    if funcSelect == 1: ## Distance Flown
                        while True:
                            groundspeed = input("Enter Groundspeed: ")
                            hours = input("Enter Hours: ")
                            min = input("Enter Minutes: ")
                            seconds = input("Enter Seconds: ")
                            try:
                                groundspeed = float(groundspeed)
                                hours = float(hours)
                                min = float(min)
                                seconds = float(seconds)
                                print(f"\n{f.distFln(groundspeed,hours,min,seconds)}") 
                                break
                            except:
                                print(numError)
                                continue
                    if funcSelect == 2: ## Top of Descent function
                        while True:
                            groundspeed = input("Enter Groundspeed: ")
                            iAlt = input("Enter Indicated Altitude: ")
                            dAlt = input("Enter Destination Altitude: ")
                            rate = input("Enter Rate (FPM): ")
                            try:
                                groundspeed = float(groundspeed)
                                iAlt = float(iAlt)
                                dAlt = float(dAlt)
                                rate = float(rate)
                                print(f"\n{f.topDscn(groundspeed,iAlt,dAlt,rate)}")
                                break
                            except:
                                print(numError)
                                continue
                    if funcSelect == 3: ##Endurance Function
                        while True:
                            fuel = input("Enter total Fuel: ")
                            fph = input("Enter fuel burn (FPH): ")
                            try:
                                fuel = float(fuel)
                                fph = float(fph)
                                print(f"\n{f.endur(fuel,fph)}")
                                break
                            except:
                                print(numError)
                    if funcSelect == 4: ## Leg time
                        while True:
                            distance = input("Enter Distance: ")
                            groundspeed = input("Enter groundspeed: ")
                            try:
                                distance = float(distance)
                                groundspeed = float(groundspeed)
                                print(f"\n{f.legTime(distance,groundspeed)}")
                                break
                            except:
                                print(numError)
                                continue
                    if funcSelect == 5: ## Specific Range
                        while True: 
                            fuel = input("Enter Fuel: ")
                            fph = input("Enter fuel burn (FPH): ")
                            gs = input("Enter groundspeed: ")
                            try:
                                fuel = float(fuel)
                                fph = float(fph)
                                gs = float(gs)
                                print(f"\n{f.spcRange(fuel,fph,gs)}")
                                break
                            except:
                                print(numError)
                                continue
                    if funcSelect == 6: ## Fuel per Hour
                        while True:
                            fuel = input("Enter total Fuel: ")
                            hour = input("Enter hours: ")
                            min = input("Enter minutes: ")
                            sec = input("Enter seconds: ")
                            try:
                                fuel = float(fuel)
                                hour = float(hour)
                                min = float(min)
                                sec = float(sec)
                                print(f"\n{f.fuelPerHour(fuel,hour,min,sec)}")
                                break
                            except:
                                print(numError)
                                continue
                    if funcSelect == 7:
                        funKill = True
                        killed = True
                        break
                if killed == True:
                    break     

            # Weight and Balance Functions WORKING                       
            elif funcGSelect == 5:
                while funKill == False:
                    funcSelect = input("\n1. Weight and Arm\n2. Weight and Moment\n3. Percent Mean Aerodynamic Chord\n4. Quit to Main Menu\n")
                    try:
                        funcSelect = int(funcSelect)
                    except:
                        print(numError)
                        continue
                    if funcSelect == 1:
                        wb.weightArm()
                    elif funcSelect == 2:
                        wb.weightMom()
                    elif funcSelect == 3:
                        wb.mac()
                    elif funcSelect == 4:
                        funKill = True
                        killed = True
                        break
                    else: 
                        print("Function not Recognized")
                if funKill == True:
                    break
      
            ## Conversion and Clock Functions WORKING
            elif funcGSelect == 6:
                while funKill == False:
                    funcSelect = input("\n1. Timer\n2. Stopwatch\n3. Convert Temperature\n4. Quit to Main Menu\n\n").lower()
                    try:
                        funcSelect = int(funcSelect)
                    except:
                        print("Error: You must enter a number\n")
                        continue
                    if funcSelect == 1:
                        print("Timer Function\nType Control-C to end")
                        hour = input("Enter Hours: ")
                        minute = input("Enter Minutes: ")
                        seconds = input("Enter Seconds: ")
                        try:
                            hour = int(hour)
                            minute = int(minute)
                            seconds = int(seconds)
                            w.timer(hour,minute,seconds)
                            break
                        except:
                            print("Error: Not all the values were integers. Enter Numbers only\n")
                            continue
                    elif funcSelect == 2:
                        w.stopwatch()
                        break
                    elif funcSelect == 3:
                        type = input("\n1. Convert Fahrenheit to Celsius\n2. Convert Celsius to Fahrenheit\n\n")
                        while True:
                            degrees = input("Enter Degrees to Convert: ")
                            try:
                                degrees = float(degrees)
                                conversion = w.tempConvert(type,degrees)
                                print(conversion)
                                break
                            except:
                                print("Error: Enter a number to convert")
                                continue
                    elif funcSelect == 4:
                        funKill = True
                        killed = True
                        break
                    else:
                        print("Error: Enter a number 1-4")
                if killed == True:
                    break
     
           
                
                
