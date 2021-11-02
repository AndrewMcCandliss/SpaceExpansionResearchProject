from Token import Token
from Boxes import Boxes
from random import Random
import matplotlib.pyplot as plt
import math
import EntropyGraph

def TokenMovementAttraction(boxesList):
    """Defines a rule for how token attraction might work, but no attraction variable is actually taken into account"""
    #"Base Chance" which affects how much a token affects the overall chance
    baseValue = 33
    #"Attraction Value" which affects how much each token is worth, negative values repulse
    attraction = -1
    for box in boxesList:
        for token in box.tokenList:
            lC = boxesList[token.pos(boxesList) - 1].GetNumTokens() * attraction + baseValue
            if (token.box == boxesList[-1]):
                rC = boxesList[0].GetNumTokens() * attraction + baseValue
            else:
                rC = boxesList[token.pos(boxesList) + 1].GetNumTokens() * attraction + baseValue
            cC = token.box.GetNumTokens() * attraction + baseValue
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

startRules = [RandomTokenPlacementSetup]
boxesRules = [BoxesChangingSplittingMerging]
tokenRules = [TokenMovementAttraction]

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
    numBoxes = len(boxesList)
    evenBoxes = [0] * numBoxes
    token = 1
    box = 0
    numTokens = CurrentNumTokens(boxesList)
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

def Graphing (boxesList):
    xList = []
    heightList = []
    for i in range(0, len(boxesList)):
        xList.append(i + 1)
        heightList.append(boxesList[i].GetNumTokens())
    plt.bar(xList, heightList)
    plt.show()

def main():
    timeSteps = 100
    startTokens = 100
    startBoxes = 5
    boxesList = startRules[0](startBoxes, startTokens)
    count = 0
    print("  Current Entropy,  Maximum Entropy")
    maxEntropy = []
    currentEntropy = []
    while (count < timeSteps):
        tokenRules[0](boxesList)
        #boxesRules[0](boxesList)
        #print(len(boxesList))
        print(CurrentEntropy(boxesList), end=', ')
        print(MaxEntropy(boxesList), end=', ')
        print(len(boxesList))
        #Graphing(boxesList)
        maxEntropy.append(MaxEntropy(boxesList))
        currentEntropy.append(CurrentEntropy(boxesList))
        count += 1
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(maxEntropy)
    ax.plot(currentEntropy)
    plt.show()


main()

