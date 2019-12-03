#You can find the puzzle here: https://adventofcode.com/2019/day/3

import sys

#The file containing every input
file = sys.argv[1]

# =====================
#        PART 1
# =====================

#Solve the first part of the puzzle:
#   - Get the instructions for each wire
#   - Get their path (and every single point they visit)
#   - Check if there are similar points visited => an intersection
#   - Get the closest intersection and return its Manhattan distance
def PartOne():
    firstWire = GetInstructions()[0]
    secondWire = GetInstructions()[1]
    firstWireCoordinates = CalculatePath(firstWire)
    secondWireCoordinates = CalculatePath(secondWire)
    listIntersections = CompareWirePaths(firstWireCoordinates, secondWireCoordinates)
    closestIntersection = GetClosestIntersection(listIntersections)
    return closestIntersection

#Get all the instructions from a txt file
def GetInstructions():
    with open(file) as f:
        lines = f.read().split("\n")
    firstWire = lines[0].split(",")
    secondWire = lines[1].split(",")
    return firstWire, secondWire

#Get the path and every single point visited of a wire
def CalculatePath(wire):
    x, y = 0, 0
    listCoordinates = [(x, y)]
    for i in range (0, len(wire)):
        if (wire[i][0] == "U"):
            j = int(wire[i][1:])
            for k in range(0, j):
                y += 1
                listCoordinates.append((x, y))
        if (wire[i][0] == "D"):
            j = int(wire[i][1:])
            for k in range(0, j):
                y -= 1
                listCoordinates.append((x, y))
        if (wire[i][0] == "L"):
            j = int(wire[i][1:])
            for k in range(0, j):
                x -= 1
                listCoordinates.append((x, y))
        if (wire[i][0] == "R"):
            j = int(wire[i][1:])
            for k in range(0, j):
                x += 1
                listCoordinates.append((x, y))
    return listCoordinates

#Get the intersections between the two wires
def CompareWirePaths(firstWire, secondWire):
    intersections = set(firstWire).intersection(secondWire)
    return list(intersections)

#Get the closest intersection (by calculating Manhattan distance's of every point) and return its Manhatthan distance
def GetClosestIntersection(intersections):
    myIntersection = intersections[1]
    for i in range(2, len(intersections)):
        if (GetAbsoluteLength(myIntersection) > GetAbsoluteLength(intersections[i])):
            myIntersection = intersections[i]
    return GetAbsoluteLength(myIntersection)

#Calculate the Manhattan distance of a coordinate
def GetAbsoluteLength(coordinates):
    absLength = abs(coordinates[0]) + abs(coordinates[1])
    return absLength

#Print the result
print(PartOne())

# =====================
#        PART 2
# =====================

#Solve the second part of the puzzle:
#   - Get the instructions for each wire
#   - Get their path (and every single point they visit + the distance travelled so far)
#   - Check if there are similar points visited => an intersection
#   - Combine intersections with the total distance travelled by each wire to reach it
#   - Get the intersection with the lowest distance travelled, and return this distance
def PartTwo():
    firstWire = GetInstructions()[0]
    secondWire = GetInstructions()[1]
    firstWireCoordinates = CalculatePathRevised(firstWire)
    secondWireCoordinates = CalculatePathRevised(secondWire)
    listIntersections = CompareWirePathsRevised(firstWireCoordinates, secondWireCoordinates)
    listWithLength = GetLengthIntersections(firstWireCoordinates, secondWireCoordinates, listIntersections)
    minimumLength = MinimumLength(listWithLength)
    return minimumLength

#Same as part 1 + the distance travelled by the wire so far
def CalculatePathRevised(wire):
    x, y , z = 0, 0, 0
    listCoordinates = [(x, y, z)]
    for i in range (0, len(wire)):
        if (wire[i][0] == "U"):
            j = int(wire[i][1:])
            for k in range(0, j):
                y += 1
                z += 1
                listCoordinates.append((x, y, z))
        if (wire[i][0] == "D"):
            j = int(wire[i][1:])
            for k in range(0, j):
                y -= 1
                z += 1
                listCoordinates.append((x, y, z))
        if (wire[i][0] == "L"):
            j = int(wire[i][1:])
            for k in range(0, j):
                x -= 1
                z += 1
                listCoordinates.append((x, y, z))
        if (wire[i][0] == "R"):
            j = int(wire[i][1:])
            for k in range(0, j):
                x += 1
                z += 1
                listCoordinates.append((x, y, z))
    return listCoordinates

#Same as part 1, revised to fit the new data structure (tuples made of 3 elements instead of 2)
def CompareWirePathsRevised(firstWire, secondWire):
    firstWireRevised = ShortenedTuples(firstWire)
    secondWireRevised = ShortenedTuples(secondWire)
    intersections = set(firstWireRevised).intersection(secondWireRevised)
    return list(intersections)

#Shorten the tuples, reducing it to two elements (remove the distance travelled)
def ShortenedTuples(list):
    slist = []
    for i in range(0, len(list)):
        slist.append(list[i][:2])
    return slist

#Get the sum of the distance travelled by the two wires for an intersection, returns a list with the coordinates and the total length
def GetLengthIntersections(firstWire, secondWire, intersections):
    listLength = []
    for i in range(0, len(intersections)):
        thisLength = 0
        for j in range(0, len(firstWire)):
            if(intersections[i] == firstWire[j][:2]):
                thisLength += firstWire[j][2]
        for k in range(0, len(secondWire)):
            if(intersections[i] == secondWire[k][:2]):                    
                thisLength += secondWire[k][2]
        listLength.append((intersections[i][0], intersections[i][1], thisLength))
    return listLength

#Get the shortest Manhatthan distance to reach an intersection
def MinimumLength(list):
    minLength = list[1][2]
    for i in range(2, len(list)):
        if (minLength > list[i][2]):
            minLength = list[i][2]
    return minLength

#Print the result
print(PartTwo())
