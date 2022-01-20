from NewToken import Token
from random import Random
import matplotlib.pyplot as plt
import math

#These are general variables that can be used by all functions
tokenList = []
boxesList = []

#Begin Defining Token Rules
def TokenMovementRandom():
    """Random Movement of Tokens"""
    for token in tokenList:
        rand = Random()
        num = rand.randint(1, 100)
        if (num <= 33):
            token.move('left', boxesList)
        elif (num > 66):
            token.move('right', boxesList)

tokenRules = [TokenMovementRandom]
#End Defining Token Rules

#Begin Defining Start Rules
def RandomTokenPlacementStart(numBoxes, numTokens):
    """Randomly sets positions of tokens in"""
    for i in range(0, numBoxes):
        boxesList.append([])
    i = 0
    rnd = Random()
    while (i < numTokens):
        token = Token(rnd.randint(0, numBoxes - 1)) #Create a token at a random position
        tokenList.append(token) #Add that token to the token list
        boxesList[token.pos].append(token) #Put the token in the box
        i += 1

def MinEntropyPlacementSetup(numBoxes, numTokens):
    """Places all tokens into a random box"""
    for i in range(0, numBoxes):
        boxesList.append([])
    i = 0
    rnd = Random().randint(0, numBoxes - 1)
    while (i < numTokens):
        token = Token(rnd) #Create a token at a the random position
        tokenList.append(token) #Add that token to the token list
        boxesList[token.pos].append(token) #Put the token in the box
        i += 1

startRules = [RandomTokenPlacementStart, MinEntropyPlacementSetup]
#End Defining Token Rules

#Begin Defining Box Rules
boxRules = []
#End Defining Box Rules

def CurrentEntropy ():
    """Finds Current Entropy"""
    h = 0
    numTokens = len(tokenList)
    for box in boxesList:
        pBox = len(box) / numTokens
        if(pBox == 0):
            h += 0
        else:
            h += -pBox * math.log(pBox)
    return h

def MaxEntropy():
    """Finds Maximum Entropy"""
    numBoxes = len(boxesList) #Finds the current number of boxes
    evenBoxes = [0] * numBoxes #Creates a list of ints the length of the boxesList
    token = 1 #Token Incrementer
    box = 0 #Box incrementer
    numTokens = len(tokenList) #Current number of tokens
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

def CircularMean():
    circularStep = (2 * math.pi) / len(boxesList)
    meanX = 0
    meanY = 0
    pos = 0
    for box in boxesList:
        circularPos = pos * circularStep
        x = math.cos(circularPos)
        y = math.sin(circularPos)
        meanX += x * len(box)
        meanY += y * len(box)
        pos += 1
    meanX /= len(tokenList)
    meanY /= len(tokenList)
    r = math.sqrt(meanX ** 2 + meanY ** 2)
    theta = math.tan(meanY / meanX)
    if (theta < 0):
        theta += 2 * math.pi
    index = theta / circularStep
    return [r, index]

def PosGraph():
    xList = []
    heightList = []
    for i in range(0, len(boxesList)):
        xList.append(i)
        heightList.append(len(boxesList[i]))
    plt.bar(xList, heightList)
    plt.show
    input("Press any key to unpause")

def IO():
    numBoxes = 0
    numTokens = 0
    print('How many boxes?')
    numBoxes = int(input())
    print('How many tokens?')
    numTokens = int(input())
    print('Real time data? [y, n]')
    printData = input()
    if (printData == 'y'):
        active = True
    else:
        active = False
    print('Which start function?')
    for i in range(0, len(startRules)):
        print(i,': ', startRules[i])
    strt = int(input())
    print('Which token function?')
    for i in range(0, len(tokenRules)):
        print(i, ': ', tokenRules[i])
    tkn = int(input())
    #print('Which box function?')
    #for i in range(0, len(boxRules)):
    #    print(i, ': ', boxRules[i])
    #box = int(input())
    print('For how long?')
    t = int(input())
    return [numBoxes, numTokens, strt, tkn, t, active]

run = True
while (run):
    vals = IO()
    numBoxes = vals[0]
    numTokens = vals[1]
    strt = vals[2]
    tkn = vals[3]
    t = vals[4]
    active = vals[5]

    maxEntropy = []
    currentEntropy = []
    startRules[strt](numBoxes, numTokens)
    print(boxesList)
    print(tokenList)
    for i in range(0, t):
        tokenRules[tkn]()
        maxEntropy.append(MaxEntropy())
        currentEntropy.append(CurrentEntropy())

        if(active):
            print('Centropy: ', CurrentEntropy(), ', ', 'Mentropy: ', MaxEntropy())
            print('Circular Mean: ', CircularMean())
            PosGraph()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(maxEntropy)
    ax.plot(currentEntropy)
    plt.show()
    again = input("Run Again? [y, n]: ")
    if(again == 'y'):
        run = True
    else:
        run = False



    