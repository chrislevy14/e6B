
"""
=============================
Main Script Runner

=============================
"""

import watch as w

while True:
    print("Welcome to the Lev6B!")
    print("Functions are selected by typing the number (type 'help' for help)\n")
    print("Select a function group: ")
    funcGroup = "1. Weather and Heading Functions\n2. Speed Functions\n 3. 'Required'/'Necessary' functions\n4. Flight Functions\n5. Weight and Balance Functions"
    funcGSelect = input(funcGroup)
    try: 
        funcGSelect = int(funcGSelect)
        break
    except:
        print("ok")
