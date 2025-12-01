import os
import sys
import inspect

circleNumbers = 100

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def readFile(file):
    file_path = currentdir+file
    with open(file_path, 'r', encoding='utf-8') as file:
        Lines = file.readlines()
    Rotations = []
    lineCount = 0
    for line in Lines:
        line = line.replace("\n", "")
        newLine = []
        newLine.append(line[0])
        newLine.append(int(line[1:]))
        Rotations.append(newLine)
        lineCount += 1
    return Rotations

def findZeros(Rotations):
    set = 50
    count0 = 0
    for line in Rotations:
        calc = "Zwischenstand ("+str(set)+"): [" + line[0]+str(line[1])
        if line[0] == 'R':
            if set == circleNumbers: 
                set = 0
            for n in range(0,line[1]):
                set += 1
                if set == 0:
                    set = set + circleNumbers
                    count0 += 1
                if set == circleNumbers:
                    set = 0
                    count0 += 1
            calc = calc+"] (R): "+str(set)
        else: 
            if set == 0:
                set = circleNumbers
            for m in range(0,line[1]):
                set -= 1
                if set == 0:
                    set = circleNumbers
                    count0 += 1
            calc = calc+"] (L): "+str(set)
        print(calc)
    return count0

print(findZeros(readFile('/InputData/day1.txt')))