import math

def readinput():
    inputs = []
    f = open("day1file.txt", "r")
    f1 = f.readlines()
    for x in f1:
        inputs.append(int(x))
    f.close()
    return inputs


def launch(module):
    mass = module
    mass = mass / 3
    mass = math.floor(mass)
    mass -= 2
    return mass

def calculatefuel(inputlist):
    a = 0
    for x in inputlist:
        a += launch(x)
        
    return a

def calculatefueloffuel(fuel):
    totalfuel = []
    fuel = launch(fuel)
    while fuel > 0:
        totalfuel.append(fuel)
        fuel = launch(fuel)
    
    return totalfuel

def calculatenewfuel(inputlist):
    fuellist = []
    totalfuel = 0
    for x in inputlist:
        fuellist = calculatefueloffuel(x)
        for y in fuellist:
            totalfuel += y

    return totalfuel

print(calculatefueloffuel(1969))
print(calculatenewfuel(readinput()))