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
    #print (rangesArray)
    for element in rangesArray:
        currLineSeparated = []
        for range_string in element:
            separated = range_string.split('-')
            currLineSeparated.append(separated)
        splitRangesArray.append(currLineSeparated)
    #print (splitRangesArray)
    return splitRangesArray[0]

def isNumberofCharactersEven(numberString):
    if len(numberString) % 2 == 0:
        return True
    else: return False

def getNumbersInRange(startNumberStr, endNumberStr):
    numbers = []
    startingNumber = int(startNumberStr)
    endingNumber = int(endNumberStr)
    for number in range (startingNumber,endingNumber+1):
        numbers.append(str(number))
    return numbers

def isInvalid(numberString):
    length = len(numberString)
    center = length // 2
    if numberString[:center] == numberString[center:]:
        return True
    else: return False

def findInvalidIDs(rangesArray):
    sumOfInvalid = 0
    for element in rangesArray:
        if isNumberofCharactersEven(element[0]) or isNumberofCharactersEven(element[1]):
            for number in getNumbersInRange(element[0], element[1]):
                if isNumberofCharactersEven(number):
                    if isInvalid(number): sumOfInvalid = sumOfInvalid + int(number)
    return sumOfInvalid

print(findInvalidIDs(separateRanges(getRanges(readFile()))))