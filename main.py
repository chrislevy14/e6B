
"""
=============================
Main Script Runner

=============================
"""

import watch as w



## Main Loop
while True:
    killed = False
    funKill = False
    print("\n\nWelcome to the Lev6B!")
    print("Functions are selected by typing the number. Type 'quit' to exit\n")

    while True:
        ## Finds Function Group
        print("Select a function group: ")
        funcGroup = "1. Weather and Heading Functions\n2. Speed Functions\n3. Required Functions\n4. Flight Functions\n5. Weight and Balance Functions\n6. Conversion and Clock Functions\n\n"
        funcGSelect = input(funcGroup)
        if funcGSelect == "quit":
            killed = True
            break
        try: 
            funcGSelect = int(funcGSelect)
            break
        except:
            print("\nError: Enter the number of the list or type 'quit' to exit")
            continue


    if killed == True:
        break

    while killed == False:
        while True:
            if funcGSelect == 1:
                a = 1

            # elif funcGSelect == 2:
            #     # Speed Functions here
            
            # elif funcGSelect == 3:
            #     # Required Functions Here
            
            elif funcGSelect == 4:
                while funKill == False:
                    funcSelect = input("\n1. Distance Flown\n2. Top of Descent\n3. Endurance\n4. Leg Time\n5. Specific Range\n6. Fuel Per Hour\n7. Quit to Main Menu")
            # elif funcGSelect == 5:
            #     #Enter Weight and Balance Functions here


            ## Conversion and Clock Functions
            elif funcGSelect == 6:
                while funKill == False:
                    funcSelect = input("\n1. Timer\n2. Stopwatch\n3. Convert Temperature\n4. Quit to Main Menu\n\n").lower()
                    if funcSelect == 'quit':
                        funKill = True
                        killed = True
                        break
                    try:
                        funcSelect = int(funcSelect)
                    except:
                        print("Error: You must enter a number\n")
                        continue

                
                    if funcSelect == 1:
                        hour = input("Enter Hours: ")
                        minute = input("Enter Minutes: ")
                        seconds = input("Enter Seconds: ")
                        try:
                            hour = int(hour)
                            minute = int(minute)
                            seconds = int(seconds)
                            w.timer(hour,minute,seconds)
                            funKill = True
                            killed = True
                            break
                        except:
                            print("Error: Not all the values were integers. Enter Numbers only\n")
                            continue
                    elif funcSelect == 2:
                        w.stopwatch()
                        funKill = True
                        killed = True
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
     
            else:
                print("Function Group Not Recognized")
