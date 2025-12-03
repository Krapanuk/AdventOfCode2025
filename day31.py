import os
import sys
import inspect

circleNumbers = 100

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def readFile():
    file_path = currentdir+'/InputData/day3.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        banks = file.readlines()
    return banks

def getBanks(banks):
    banksArray = []
    for bank in banks:
        banksArray.append(bank)
    return banksArray

def findHighestJoltageCombi(bank):
    joltageCombi = 0
    for leftElement in range(0,len(bank)):
        for rightElement in range(leftElement+1,len(bank)+1):
            if leftElement != rightElement-1:
                #print("LeftElem: "+ bank[leftElement:leftElement+1] + " RightElem: "+ bank[rightElement-1:rightElement])
                combinedNumber = int(bank[leftElement:leftElement+1]+bank[rightElement-1:rightElement])
                if (combinedNumber) > joltageCombi: joltageCombi = combinedNumber
    return joltageCombi

def sumJoltageCombis(banksArray):
    joltageSum = 0
    for bank in banksArray: joltageSum = joltageSum + findHighestJoltageCombi(bank)
    return joltageSum

print(sumJoltageCombis(getBanks(readFile())))
#print(findHighestJoltageCombi('8191'))