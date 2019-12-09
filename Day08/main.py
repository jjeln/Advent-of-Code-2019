#You can find the puzzle here: https://adventofcode.com/2019/day/8
import sys

#The file containing every input
file = sys.argv[1]
#x and y size of the picture
xSize = int(sys.argv[2])
ySize = int(sys.argv[3])

def Main():
    myResult = GetLayers(GetInputs())
    #Part 1 solution
    myListZero = CompareNumberOfN(myResult, 0)
    print("Part 1 answer is: " + str(myListZero.count(1) * myListZero.count(2)))
    #Part 2 solution
    myCombinedList = CombineLayers(myResult)
    myPicture = GetPixels(myCombinedList)
    print("Part 2 answer is:\n" + DrawPicture(myPicture).replace("0", " "))

# =====================
#        PART 1
# =====================

#Geting all the numbers from a txt file
def GetInputs():
    with open(file) as f:
        inputs = f.read().splitlines()
    listInputs = []
    for n in range(0, len(inputs[0])):
        listInputs.append(int(inputs[0][n]))
    return listInputs

#Separate the numbers into different layers
def GetLayers(listPixels):
    allLayers = []
    cursor = 0
    newLayer = []
    while cursor < len(listPixels)-1 :
        newLayer, cursor = GetSingleLayer(listPixels, cursor)
        allLayers.append(newLayer)
    return allLayers

#Get a single layer of numbers
def GetSingleLayer(listPixels, cursor):
    myCurrentLayer = []
    for y in range(0, ySize):
        for x in range(0, xSize):
            myCurrentLayer.append(listPixels[cursor])
            cursor += 1
    return(myCurrentLayer, cursor)

#Compare the number of N number in every layer, then return the one with the less occurences 
def CompareNumberOfN(list, n):
    myList = []
    nCount = 999999
    for i in list:
        if i.count(n) < nCount:
            myList = i
            nCount = i.count(n)
    return myList

# =====================
#        PART 2
# =====================

#Flatten the layers, and turn all their digits into a string of digits
def CombineLayers(list):
    myCombinedLayer = []
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            if(i == 0):
                myCombinedLayer.append(str(list[i][j]))
            else:
                myCombinedLayer[j] += str(list[i][j])
    return myCombinedLayer

#Get the pixel of the flattened layer
#Remove transparent pixels from every string, then pick the first color/number on the top
def GetPixels(list):
    myPicture = ""
    for i in list:
        myPicture += i.replace("2", "")[0]
    return myPicture

#Turn every white pixel transparent for better visibility
def DrawPicture(string):
    return '\n'.join(string[i:i+25] for i in range(0, len(string), 25))

Main()
