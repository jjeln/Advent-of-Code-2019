#You can find the puzzle here: https://adventofcode.com/2019/day/6

import sys

#The file containing every input
file = sys.argv[1]

#Geting all the numbers from a txt file
def GetInputs():
    dataInput = {}
    dataValues = {}
    with open(file) as f:
        listInputs = f.read().splitlines()
    for i in listInputs:
        j = i.split(")")
        if j[0] not in dataInput:
            dataInput[j[0]] = []
            dataInput[j[0]].append(j[1])
        else:
            dataInput[j[0]].append(j[1])
        if j[0] not in dataValues: dataValues[j[0]] = 0
        if j[1] not in dataValues: dataValues[j[1]] = 0
    return dataInput, dataValues

def GetDataValue(data, values):
    for i in data:
        for j in range(0, len(data[i])):
            if data[i][j] in values:
                values[data[i][j]] += 1 + values[i]
    sumDict = GetSumDict(values)
    return sumDict

def GetSumDict(dict):
    s = 0
    for i in dict:
        s += dict[i]
    return s

print(GetDataValue(GetInputs()[0], GetInputs()[1]))
