import os
import sys
import inspect

circleNumbers = 100

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def readFile():
    count0 = 0
    file_path = currentdir+'/InputData/day1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        Lines = file.readlines()
    Rotations = []
    lineCount = 0
    for line in Lines:
        line = line.replace("\n", "")
        newLine = []
        newLine.append(line[0])
        print("line: " + line)
        if len(line) < 3:
            value = int(line[-1:])
            newLine.append(value)
            #print("value: "+ str(value))
        else: 
            newLine.append(int(line[-2:]))
            #print("value: "+ str(int(line[-2:])))
        Rotations.append(newLine)
        lineCount += 1
    return Rotations, count0
	
def rotateRight(set, rotations):
    rotate = set + rotations
    if rotate == 100:
        rotate = 0
    if rotate > 100:
        rotate = rotate % 100
    return rotate

def rotateLeft(set, rotations):
    rotate = set - rotations
    if rotate < 0:
        rotate = circleNumbers + rotate
    if rotate == 100:
        rotate = 0
    return rotate

def findLast(input):
    Rotations = input[0]
    count0 = input[1]
    set = 50
    for line in Rotations:
        value = line[1]
        #print("value: "+str(set))
        if line[0] == 'R':
            set = rotateRight(set, value)
            print("Zwischenstand: "+str(set))
        else: 
            set = rotateLeft(set, value)
            print("Zwischenstand: "+str(set))
        if set == 0 or set == 100:
            count0 += 1
    return count0

print(findLast(readFile()))