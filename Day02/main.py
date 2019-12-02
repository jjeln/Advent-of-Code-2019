#You can find the puzzle here: https://adventofcode.com/2019/day/2

import sys

#The file containing every input
file = sys.argv[1]

#Our target number used in part 2 to find the noun and verb
if(len(sys.argv) > 2):
    target = sys.argv[2]
else:
    target = -1
target = int(target)

# =====================
#        PART 1
# =====================



#Get all the masses from a txt file
def GetInputs(x, y):
    with open(file) as f:
        listInputs = f.read().split(",")
    for n in range(0, len(listInputs)):
        listInputs[n] = int(listInputs[n])
    CorrectInputs(listInputs, x, y)
    return listInputs

#Changes the values of list[1] and list[2]. They're always the same in part 1, but they can change in part 2
def CorrectInputs(list, x, y):
    list[1] = x
    list[2] = y
    return list

#Does a set of operation on the list given in argument.
#We use a cursor to manipulate its content, as every operation is related to the cursor position in the list.
#See the puzzle instructions for more info
def ReadList(list):
    cursor = 0
    message = ""
    inProgress = True
    while inProgress == True:
        if cursor >= len(list):
            message = list[0]
            inProgress = False
        elif list[cursor] == 1:
            p1 = list[cursor + 1]
            p2 = list[cursor + 2]
            p3 = list[cursor + 3]
            list[p3] = list[p1] + list[p2]
            cursor += 4
        elif list[cursor] == 2:
            p1 = list[cursor + 1]
            p2 = list[cursor + 2]
            p3 = list[cursor + 3]
            list[p3] = list[p1] * list[p2]
            cursor += 4
        elif list[cursor] == 99:
            message = list[0]
            inProgress = False
        else:
            message = "ERROR: NUMBER UNKNOWN"
            inProgress = False
    return message;


# =====================
#        PART 2
# =====================

#Use two for loops to check the possible results of ReadList() when you change the 1 et 2 index values of its list. We're looking for the values giving list[0] the value of the variable target
def FindNounAndVerb(target):
    i = 0
    j = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if(ReadList(GetInputs(i, j)) == target):
                break
            j+= 1;
        if(ReadList(GetInputs(i, j)) == target):
            break
        i+= 1;
    return("The nound is: " + str(i) + "\nAnd the verb is: " + str(j))  


# =====================
#    THE RESULTS
# =====================

#Checks the number of arguments: if there is just one, it means we're looking for the part 1 solution. If there are two, we're looking for the part 2 solution.
#Part 2 Solution
if(target >= 0):
    print(FindNounAndVerb(target))
#Part 1 Solution
else:
    print(ReadList(GetInputs(12, 2)))

