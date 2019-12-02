#You can find the puzzle here: https://adventofcode.com/2019/day/1

import math
import sys

#The file containing every masses
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Calculate the total fuel required
def FuelRequired():
    masses = GetMasses()
    fuelRequired = 0
    for m in masses:
        fuelRequired += FuelRequiredPerModule(int(m))
    return fuelRequired

#Calculate the fuel requirement for a single module
def FuelRequiredPerModule(mass):
    fuelRequiredForModule = math.floor(mass / 3) - 2
    if fuelRequiredForModule < 0:
        fuelRequiredForModule = 0
    return fuelRequiredForModule

#Get all the masses from a txt file
def GetMasses():
    with open(filename) as f:
        listMasses = f.read().splitlines()
        return listMasses

print(FuelRequired())

# =====================
#        PART 2
# =====================

#Calculate the total fuel required for the second version
def FuelRequiredV2():
    masses = GetMasses()
    fuelRequired = 0
    for m in masses:
        fuelRequired += FuelRequiredPerModuleV2(int(m))
    return fuelRequired

#Calculate the fuel requirement for a single module (and the fuel requirements for the fuel, etc...)
def FuelRequiredPerModuleV2(mass):
    r = 0
    n = mass
    while n > 0:
        n = math.floor(n / 3) - 2
        if n < 0:
            n = 0
        r += n
    return r

print(FuelRequiredV2())
