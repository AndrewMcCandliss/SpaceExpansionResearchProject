from Token import Token
from Boxes import Boxes
from random import Random
import matplotlib.pyplot as plt
import math
import EntropyGraph

def TokenMovementRandom(boxesList):
    """Random."""
    for box in boxesList:
        for token in box.tokenList:
            rand = Random()
            num = rand.randint(1, 100)
            if(num <= 33):
                token.move('left', boxesList)
            elif (num > 66):
                token.move('right', boxesList)


def BoxesChangingSplittingMerging(boxesList):
    """Defines a basic rule to make boxes split and merge, not meant to be final, just testing some stuff out"""
    i = 0
    while (i < len(boxesList)):
        box = boxesList[i]
        rand = Random()
        d100 = rand.randint(1,100)
        splitFactor = 2 #Changes how much the number of tokens affects splitting chance
        if(d100 < box.GetNumTokens() * splitFactor): # splitting chance rises with the amount of tokens in the box
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
    """Randomly places an amount of tokens into an amount of boxes, then returns a list of boxes"""
    boxesList = []
    for i in range(0, numBoxes):
        boxesList.append(Boxes([]))
    rnd = Random()
    for i in range(0, numTokens):
        token = Token(boxesList[rnd.randint(0, numBoxes - 1)])
        token.box.tokenList.append(token)
    return boxesList

def MinEntropyPlacementSetup(numBoxes, numTokens):
    """Places all tokens into box 0, creates every box"""
    boxesList = []
    for i in range(0, numBoxes):
        boxesList.append(Boxes([]))
    for i in range(0, numTokens):
        token = Token(boxesList[0])
        token.box.tokenList.append(token)
    return boxesList

startRules = [RandomTokenPlacementSetup, MinEntropyPlacementSetup]
boxesRules = [BoxesChangingSplittingMerging]
tokenRules = [TokenMovementRandom]

def CurrentNumTokens(boxesList):
    numTokens = 0
    for box in boxesList:
        numTokens += box.GetNumTokens()
    return numTokens

def CurrentEntropy (boxesList):
    """Finds the current entropy"""
    h = 0
    numTokens = CurrentNumTokens(boxesList)
    for box in boxesList:
        pBox = box.GetNumTokens() / numTokens
        if(pBox == 0):
            h += 0
        else:
            h += -pBox * math.log(pBox)

    return h
def MaxEntropy (boxesList):
    """Finds maximum entropy using the more detailed algorithm"""
    numBoxes = len(boxesList) #Finds the current number of boxes
    evenBoxes = [0] * numBoxes #Creates a list of ints the length of the boxesList
    token = 1 #Token Incrementer
    box = 0 #Box incrementer
    numTokens = CurrentNumTokens(boxesList) #Current number of tokens
    while(token <= numTokens): #Starts at 1 and ends at the last token
        if(box >= numBoxes): #Restarts box incrementer
            box = 0
        evenBoxes[box] += 1 #Adds 1 token to the current box increment
        box += 1 #Increases box increment
        token += 1 #Increases token incrememnt
    hMax = 0
    for val in evenBoxes:
        pBox = val / numTokens
        if (pBox == 0):
            hMax += 0
        else:
            hMax += -pBox * math.log(pBox)
    return hMax

def Graphing (boxesList):
    xList = []
    heightList = []
    for i in range(0, len(boxesList)):
        xList.append(i + 1)
        heightList.append(boxesList[i].GetNumTokens())
    plt.bar(xList, heightList)
    plt.show()

def CircularMean (boxesList):
    circularStep = (2 * math.pi) / len(boxesList)
    meanX = 0
    meanY = 0
    for box in boxesList:
        circularPos = box.GetPos(boxesList) * circularStep
        x = math.cos(circularPos)
        y = math.sin(circularPos)
        meanX += x * box.GetNumTokens()
        meanY += y * box.GetNumTokens()
    meanX /= CurrentNumTokens(boxesList)
    meanY /= CurrentNumTokens(boxesList)
    r = math.sqrt(math.pow(meanX, 2) + math.pow(meanY, 2))
    theta = math.tan(meanY / meanX)
    if (theta < 0):
        theta += 2 * math.pi
    index = theta / circularStep
    return [r, index]

def main():
    timeSteps = 100
    startTokens = 100
    startBoxes = 10
    boxesList = startRules[1](startBoxes, startTokens)
    count = 0
    print("  Current Entropy,  Maximum Entropy")
    maxEntropy = []
    currentEntropy = []
    while (timeSteps > count):
        tokenRules[0](boxesList)
        #boxesRules[0](boxesList)
        print(CurrentEntropy(boxesList), end=', ')
        print(MaxEntropy(boxesList), end=', ')
        #print(len(boxesList))
        maxEntropy.append(MaxEntropy(boxesList))
        currentEntropy.append(CurrentEntropy(boxesList))
        print(CircularMean(boxesList))
        #Graphing(boxesList)
        count += 1
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(maxEntropy)
    ax.plot(currentEntropy)
    plt.show()
    Graphing(boxesList)


main()

