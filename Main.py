from Token import Token
from Boxes import Boxes
from random import Random
import matplotlib.pyplot as plt
import math


def TokenMovementAttraction(boxesList):
    """Defines a rule for how token attraction might work, but no attraction variable is actually taken into account"""
    for box in boxesList:
        for token in box.tokenList:
            lC = boxesList[token.pos(boxesList) - 1].GetNumTokens() + 1
            if (token.box == boxesList[-1]):
                rC = boxesList[0].GetNumTokens() + 1
            else:
                rC = boxesList[token.pos(boxesList) + 1].GetNumTokens() + 1
            cC = token.box.GetNumTokens() + 1
            lChance = (lC * 100 ) / (lC + rC + cC)
            rChance = (rC * 100 ) / (lC + rC + cC)
            cChance = (cC * 100 ) / (lC + rC + cC)
            rand = Random()
            d100 = rand.randint(1, 100)
            if(d100 <= lChance):
                token.move('left', boxesList)
                # print('token moves left')
            elif(d100 > 100 - rChance):
                token.move('right', boxesList)
                # print('token moves right')
            # else:

                # print("token doesn't move")

def BoxesChangingSplittingMerging(boxesList):
    """Defines a basic rule to make boxes split and merge, not meant to be final, just testing some stuff out"""
    i = 0
    while (i < len(boxesList)):
        box = boxesList[i]
        rand = Random()
        d100 = rand.randint(1,100)
        if(d100 < box.GetNumTokens()): # splitting chance rises with the amount of tokens in the box
            splitList = box.tokenList
            middleIndex = len(splitList) // 2
            aList = splitList[:middleIndex]
            bList = splitList[middleIndex:]
            box.tokenList = aList
            newBox = Boxes(bList)
            for token in bList:
                token.box = newBox
            boxesList.insert(i + 1, newBox)
        else: # merging chance rises if the difference in amounts of tokens in the current box and the next box is high
            numTokens = box.GetNumTokens()
            d100 = rand.randint(1,100)
            if(d100 < 25 * (numTokens / (boxesList[i - 1].GetNumTokens() + 1 )) and len(boxesList) > 1): # Checks left
                tokensMerging = boxesList[i - 1].tokenList
                for token in tokensMerging:
                    token.box = box
                box.tokenList.extend(tokensMerging)
                boxesList.remove(boxesList[i - 1])
                i -= 1

            rightBox = Boxes([])
            box = boxesList[i]
            if (box == boxesList[-1]):
                rightBox = boxesList[0]
            else:
                rightBox = boxesList[i + 1]


            if(d100 < 25 * (numTokens / (rightBox.GetNumTokens() + 1)) and len(boxesList) > 1): # Checks Right
                tokensMerging = rightBox.tokenList
                for token in tokensMerging:
                    token.box = box
                box.tokenList.extend(tokensMerging)
                boxesList.remove(rightBox)
                
        i += 1


def RandomTokenPlacementSetup(numBoxes, numTokens):
    boxesList = []
    for i in range(0, numBoxes):
        boxesList.append(Boxes([]))
    rnd = Random()
    for i in range(0, numTokens):
        token = Token(boxesList[rnd.randint(0, numBoxes - 1)])
        token.box.tokenList.append(token)
    return boxesList

startRules = [RandomTokenPlacementSetup]
boxesRules = [BoxesChangingSplittingMerging]
tokenRules = [TokenMovementAttraction]

def CurrentNumTokens(boxesList):
    numTokens = 0
    for box in boxesList:
        numTokens += box.GetNumTokens()
    return numTokens

def CurrentEntropy (boxesList, numTokens):
    """Finds the current entropy"""
    h = 0
    for box in boxesList:
        pBox = box.GetNumTokens() / numTokens
        if(pBox == 0):
            h += 0
        else:
            h += -pBox * math.log(pBox)

    return h
def MaxEntropy (boxesList, numTokens):
    """Finds maximum entropy using the more detailed algorithm"""
    numBoxes = len(boxesList)
    evenBoxes = [0] * numBoxes
    token = 1
    box = 0
    while(token <= numTokens):
        if(box >= numBoxes):
            box = 0
        evenBoxes[box] += 1
        box += 1
        token += 1
    hMax = 0
    for val in evenBoxes:
        pBox = val / numTokens
        if (pBox == 0):
            hMax += 0
        else:
            hMax += -pBox * math.log(pBox)
    return hMax

def main():
    timeSteps = 100
    startTokens = 100
    startBoxes = 5
    boxesList = startRules[0](startBoxes, startTokens)
    count = 0
    print("  Current Entropy,  Maximum Entropy")
    while (count < timeSteps):
        #tokenRules[0](boxList)
        #boxesRules[0](boxList)
        #print(len(boxList))
        print(CurrentEntropy(boxesList, startTokens), end=', ')
        print(MaxEntropy(boxesList, startTokens))
        count += 1


main()

