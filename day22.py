import os
import sys
import inspect

circleNumbers = 100

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def readFile():
    file_path = currentdir+'/InputData/day2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        Lines = file.readlines()
    return Lines

def getRanges(Lines):
    rangesArray = []
    for line in Lines:
        ranges = line.strip().split(',')
        rangesArray.append(ranges)
    return rangesArray

def separateRanges(rangesArray):
    splitRangesArray = [] 
    for element in rangesArray:
        currLineSeparated = []
        for range_string in element:
            separated = range_string.split('-')
            currLineSeparated.append(separated)
        splitRangesArray.append(currLineSeparated)
    return splitRangesArray[0]

def getNumbersInRange(startNumberStr, endNumberStr):
    numbers = []
    startingNumber = int(startNumberStr)
    endingNumber = int(endNumberStr)
    for number in range (startingNumber,endingNumber+1):
        numbers.append(str(number))
    return numbers

def isNumberofCharactersEven(numberString):
    if len(numberString) % 2 == 0:
        return True
    else: return False

def isEachNumberTheSame(numberString, stepRange, repetitions):
    #print(numberString + " Steps: "+ str(stepRange) + "Rep: " +str(repetitions))
    same = True #3,2,1 => stepRange  - 2-1,3-1,6-1 => repetitions
    for i in range (1,repetitions):
        if numberString[(i-1)*stepRange:i*stepRange] != numberString[i*stepRange:(i+1)*stepRange]: same = False
        #print("Comparison: ["+ str(numberString[((i-1)*stepRange):(i*stepRange)]) + "] to [" +str(numberString[i*stepRange:(i+1)*stepRange])+ "]")
        #Range 1: numberString[0:0] == numberString[1:1]
        #Range 1: numberString[1:1] == numberString[2:2]
        #...
        #Range 2: numberString[0:1] == numberString[2:3]
        #Range 2: numberString[2:3] == numberString[4:5]
        #...
        #Range 3: numberString[0:2] == numberString[3:5]
    return same


#Splits
#2 => 11
#3 => 111
#4 => 1111, 1212
#5 => 11111
#6 => 111111, 121212, 123123
#7 => 1111111
#8 => 11111111, 12121212, 12341234

def isInvalid(numberString):
    isInvalid = False
    numberLength = len(numberString) #6
    for n in range(1, numberLength): #5,4,3,2,1
        if numberLength % n == 0: #3, 2, 1
            test = numberLength // n
            if isEachNumberTheSame(numberString, n, test): isInvalid = True    
    return isInvalid

def findInvalidIDs(rangesArray):
    sumOfInvalid = 0
    for element in rangesArray:
        for number in getNumbersInRange(element[0], element[1]):
            if isInvalid(number): sumOfInvalid = sumOfInvalid + int(number)              
    return sumOfInvalid

print(findInvalidIDs(separateRanges(getRanges(readFile()))))