#You can find the puzzle here: https://adventofcode.com/2019/day/5

import sys

#The file containing every input
file = sys.argv[1]
#Your input
userInput = int(sys.argv[2])

#Geting all the numbers from a txt file
def GetInputs():
    with open(file) as f:
        listInputs = f.read().split(",")
    for n in range(0, len(listInputs)):
        listInputs[n] = int(listInputs[n])
    return listInputs

#Turn a number into a list of digits for the parameter modes
def GetDigits(i):
    s = format(i, '05d')
    pListDigits = ["", "", "", "", ""]
    for i in range (0, len(s)):
        pListDigits[i] = s[i]
    listDigits = [0, 0, 0, 0]
    listDigits[-1] = int(pListDigits[-2] + pListDigits[-1])
    for j in range (0, 3):
        if (pListDigits[j] != ""):
            listDigits[j] = int(pListDigits[j])
        else:
            listDigits[j] = 0
    return listDigits

#Work on the list of numbers, loop on it to find an output
def ReadList(list):
    cursor = 0
    myLength = len(list)
    message = ""
    inProgress = True
    while inProgress == True:
        if (cursor >= myLength):
            message = list[0]
            inProgress = False
        elif len(str(list[cursor])) > 2:
            cursor, list, message, inProgress = ParameterMode(cursor, list, message, inProgress)
        else:
            cursor, list, message, inProgress = SetOpCode(cursor, list, message, inProgress, list[cursor + 1], list[cursor + 2], list[cursor + 3])
    return message;

#Work on the list of numbers, launch a function depending on the opcode
def SetOpCode(cursor, list, message, inProgress, a1, a2, a3):
    if list[cursor] == 1:
        cursor, list = Calc1(cursor, list, a1, a2, a3)
    elif list[cursor] == 2:
        cursor, list = Calc2(cursor, list, a1, a2, a3)
    elif list[cursor] == 3:
        cursor = Input3(cursor, list, a1)
    elif list[cursor] == 4:
        cursor = Output4(cursor, list, a1)
    elif list[cursor] == 5:
        cursor = Jump5(cursor, list, a1, a2)
    elif list[cursor] == 6:
        cursor = Jump6(cursor, list, a1, a2)
    elif list[cursor] == 7:
        cursor, list = Store7(cursor, list, a1, a2, a3)
    elif list[cursor] == 8:
        cursor, list = Store8(cursor, list, a1, a2, a3)
    elif list[cursor] == 99:
        message = list[0]
        inProgress = False
    else:
        message = "ERROR: NUMBER UNKNOWN"
        inProgress = False
    return cursor, list, message, inProgress

#Decipher an opcode in parameter mode, then launch SetOpCode()
def ParameterMode(cursor, list, message, inProgress):
    myParam = int(GetDigits(list[cursor])[3])
    if(int(GetDigits(list[cursor])[2]) == 0):
        a1 = list[cursor + 1]
    else:
        a1 = cursor + 1
    if(int(GetDigits(list[cursor])[1]) == 0):
        a2 = list[cursor + 2]
    else:
        a2 = cursor + 2
    if(int(GetDigits(list[cursor])[0]) == 0):
        a3 = list[cursor + 3]
    else:
        a3 = cursor + 3
    list[cursor] = myParam
    cursor, list, message, inProgress = SetOpCode(cursor, list, message, inProgress, a1, a2, a3)
    return cursor, list, message, inProgress

def Calc1(cursor, list, p1, p2, p3):
    list[p3] = list[p1] + list[p2]
    cursor += 4
    return cursor, list

def Calc2(cursor, list, p1, p2, p3):
    list[p3] = list[p1] * list[p2]
    cursor += 4
    return cursor, list

def Input3(cursor, list, p1):
    list[p1] = userInput
    cursor += 2
    return cursor

def Output4(cursor, list, p1):
    print("Output is: " + str(list[p1]))
    cursor += 2
    return cursor

def Jump5(cursor, list, p1, p2):
    if(list[p1] != 0):
        cursor = list[p2]
    else:
        cursor += 3
    return cursor

def Jump6(cursor, list, p1, p2):
    if(list[p1] == 0):
        cursor = list[p2]
    else:
        cursor += 3
    return cursor

def Store7(cursor, list, p1, p2, p3):
    if(list[p1] < list[p2]):
        list[p3] = 1
    else:
        list[p3] = 0
    cursor += 4
    return cursor, list

def Store8(cursor, list, p1, p2, p3):
    if(list[p1] == list[p2]):
        list[p3] = 1
    else:
        list[p3] = 0
    cursor += 4
    return cursor, list

print(ReadList(GetInputs()))
