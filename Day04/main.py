import sys

#The file containing the puzzle input has to be given as an argument on the command line
file = sys.argv[-1]

# =====================
#        PART 1
# =====================

#   - Get the password range from a file
#   - Get the number of matching password and return it
def PartOne():
    min = int(GetData(file)[0])
    max = int(GetData(file)[1])
    numberOfSolutions = HowManySolutions(min, max)
    return numberOfSolutions

#Get the data (the password range) from a file
def GetData(file):
    with open(file) as f:
        data = f.read().split("-")
    return data

#Return the number of matching password after checking them one by one (see IsThisCodeValid(i) for more info)
def HowManySolutions(min, max):
    nSolutions = 0
    #currentNumber = min
    for currentNumber in range(min, max):
        if (IsThisCodeValid(currentNumber) == True):
            nSolutions += 1
    return nSolutions

#Check if the password would work by:
#   - Looking if the next digit is bigger
#   - Looking if there is a groupe of *at least* two matching digits
def IsThisCodeValid(i):
    myCode = GetDigits(i)
    isMyCodeValid = True
    sameDigitFound = False
    for n in range(0, len(myCode) - 1):
        if (myCode[n] > myCode[n + 1]):
            isMyCodeValid = False
        if (myCode[n] == myCode[n + 1]):
            sameDigitFound = True
    if(sameDigitFound == False):
        isMyCodeValid = False
    return isMyCodeValid

#Take a 6 digits number and turn int into a list of 6 single digit numbers
def GetDigits(i):
    s = str(i)
    listDigits = [int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5])]
    return listDigits

#Print the solution
print(PartOne())

# =====================
#        PART 2
# =====================

#The only difference between part 1 and 2 is the IsThisCodeValid function: I modified it to search for groups of more than two matching digits
def PartTwo():
    min = int(GetData(file)[0])
    max = int(GetData(file)[1])
    numberOfSolutions = HowManySolutionsRevised(min, max)
    return numberOfSolutions

def HowManySolutionsRevised(min, max):
    nSolutions = 0
    #currentNumber = min
    for currentNumber in range(min, max):
        if (IsThisCodeValidRevised(currentNumber) == True):
            nSolutions += 1
    return nSolutions

#Instead of only looking for adjacent characters, I'm now looking for n+2 and n-2 characters
def IsThisCodeValidRevised(i):
    myCode = GetDigits(i)
    isMyCodeValid = True
    sameDigitFound = False
    for n in range(0, len(myCode) - 1):
        if (myCode[n] > myCode[n + 1]):
            isMyCodeValid = False
        if(n > 0 and n < len(myCode) - 1):
            if((n < len(myCode) - 2) and (n > 1)):
                if((myCode[n] == myCode[n + 1] and myCode[n] != myCode[n - 1]) or (myCode[n] == myCode[n - 1] and myCode[n] != myCode[n + 1])):
                    if ((myCode[n] != myCode[n + 2]) and (myCode[n] != myCode[n - 2])):
                        sameDigitFound = True
            elif(n < len(myCode) - 2):
                if((myCode[n] == myCode[n + 1] and myCode[n] != myCode[n - 1]) or (myCode[n] == myCode[n - 1] and myCode[n] != myCode[n + 1])):
                    if (myCode[n] != myCode[n + 2]):
                        sameDigitFound = True
            elif(n > 1):
                if((myCode[n] == myCode[n + 1] and myCode[n] != myCode[n - 1]) or (myCode[n] == myCode[n - 1] and myCode[n] != myCode[n + 1])):
                    if (myCode[n] != myCode[n - 2]):
                        sameDigitFound = True
    if(sameDigitFound == False):
        isMyCodeValid = False
    return isMyCodeValid

#Print the solution
print(PartTwo())
