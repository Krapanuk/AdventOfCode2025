import os
import sys
import inspect

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
        bank = bank.strip()
        banksArray.append(bank)
    #print(banksArray)
    return banksArray

def findHighestJoltageCombi(bank):
    #print("X: "+str(bank))
    #stayCount=0
    pos = 0
    maxLength = len(bank)-1
    delCount = len(bank)-12
    #print("Init delCount: "+str(delCount))
    while pos < maxLength:
        #print("While: "+str(pos)+" < "+str(maxLength))
        #print(pos-stayCount)
        #print(bank)
        if bank[pos] < bank[pos+1]:
            bank = bank[:pos] + bank[pos+1:]
            maxLength = len(bank)-1
            pos -= 2
            delCount -= 1
            #print("delCount: "+str(delCount))
            if delCount == 0: break
        pos += 1
    if len(bank) > 12: bank = bank[:12]
    return int(bank)

def sortBatteriesAscending(bank):
    numbersAndPos = []
    for digit in range(0,10):
        for pos in range(0,len(bank)):
            if bank[pos] == str(digit):
                numbersAndPos.append([digit, pos])
    return numbersAndPos

def sumJoltageCombis(banksArray):
    #print(banksArray)
    joltageSum = 0
    bankCount = 0
    for bank in banksArray: 
        bankCount += 1
        print(bankCount)
        joltageSum = joltageSum + findHighestJoltageCombi(bank)
    return joltageSum

print(sumJoltageCombis(getBanks(readFile())))
#print(findHighestJoltageCombi('987654321111111'))
#print(findHighestJoltageCombi('234234234234278'))
#print(findHighestJoltageCombi('811111111111119'))