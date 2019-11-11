"""
=============================================
##  Weight and Balance Class  ##

Contains weight and balance functions

Christos Levy 2019
=============================================
"""
def inf():
    while True:
        yield


## Calculates the CG, total moment and total weight
def weightArm():
    WeightList = []
    totalMoment = 0
    centerGravity = 0
    for i in inf():
        weight = input("Enter Weight: ")
        arm = input("Enter Arm: ")
        try:
            weight = float(weight)
            arm = float(arm)
            moment = weight*arm
            WeightList.append(weight)
            totalWeight = sum(WeightList)
            totalMoment += moment
            if totalWeight == 0:
                centerGravity += 0
            else:
                centerGravity += totalMoment/totalWeight
        except:
            print("Error: Values were not numbers")
            continue
        print(f"\nMOMENT: {totalMoment}\nGROSS WEIGHT: {totalWeight}\nCG: {round(centerGravity,2)}")
        goAgain = input("Press Enter to enter another value or type '/'+ enter to quit:\n")
        if goAgain == "":
            continue
        else:
            print(f"MOMENT: {totalMoment}\nGROSS WEIGHT: {totalWeight}\nCG: {round(centerGravity,2)}\n")
            break


## Calculates the CG, total moment and total weight without asking for arm
def weightMom():
    WeightList = []
    totalMoment = 0
    centerGravity = 0
    for i in inf():
        weight = input("Enter Weight: ")
        moment = input("Enter Moment: ")
        try:
            weight = float(weight)
            moment = float(moment)
            WeightList.append(weight)
            totalWeight = sum(WeightList)
            totalMoment += moment
            centerGravity += totalMoment/totalWeight
        except:
            print("Error: Values were not numbers")
            continue
        print(f"\nMOMENT: {totalMoment}\nGROSS WEIGHT: {totalWeight}\nCG: {round(centerGravity,2)}")
        goAgain = input("Press Enter to enter another value or type '/'+ enter to quit:\n")
        if goAgain == "":
            continue
        else:
            print(f"MOMENT: {totalMoment}\nGROSS WEIGHT: {totalWeight}\nCG: {round(centerGravity,2)}\n")
            break

## Calculates the percent of the mean aerodynamic chord
def mac():
    for i in inf():
        cg = input("Enter CG: ")
        Lemac = input("Enter Leading Edge Mean Aerodynamic Chord: ")
        mac = input("Enter mean aerodynamic chord: ")
        try:
            cg = float(cg)
            Lemac = float(Lemac)
            mac = float(mac)
            if mac == 0:
                print("Error: MAC Cannot be 0")
                continue
            else:
                percentMac = ((cg - Lemac)/mac)*100
                print(f"Percent MAC: {round(percentMac,1)}%")
                break
        except:
            print("Error: Values were not numbers")
            continue
