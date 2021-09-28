from Token import Token
from random import Random
from Boxes import Boxes

def TokenMovementAttraction(boxesList, TokenList):
    """Defines a rule for how token attraction might work, but no attraction variable is actually taken into account"""
    for token in TokenList:
        lC = boxesList[token.pos - 1].GetNumTokens() + 1
        if (token.pos == len(boxesList) - 1):
            rC = boxesList[0].GetNumTokens() + 1
        else:
            rC = boxesList[token.pos + 1].GetNumTokens() + 1
        cC = boxesList[token.pos].GetNumTokens() + 1
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
                token.pos = i + 1
                token.box = newBox
            boxesList.insert(i + 1, newBox)
        else: # merging chance rises if the difference in amounts of tokens in the current box and the next box is high
            numTokens = box.GetNumTokens()
            if(d100 < 25 * (numTokens / (boxesList[i - 1].GetNumTokens() + 1))): # Checks left
                tokensMerging = boxesList[i - 1].tokenList
                for token in tokensMerging:
                    token.box = box
                for token in box.tokenList:
                    token.pos = i - 1
                box.tokenList.extend(tokensMerging)
                boxesList.remove(boxesList[i - 1])
                i -= 1

            rightBox = Boxes([])
            box = boxesList[i]
            if (box == boxesList[-1]):
                rightBox = boxesList[0]
            else:
                rightBox = boxesList[i + 1]


            if(d100 < 25 * (numTokens / (rightBox.GetNumTokens() + 1))): # Checks Right
                tokensMerging = rightBox.tokenList
                for token in tokensMerging: # if rightbox is index 0 problems will be caused with the token.pos, fix that
                    token.pos = i
                    token.box = box
                box.tokenList.extend(tokensMerging)
                boxesList.remove(rightBox)
                i -= 1
        i += 1



boxesRules = [BoxesChangingSplittingMerging]
TokenRules = [TokenMovementAttraction]

def main():
    timeSteps = 100
    tokens = 100
    boxList = [Boxes([])]
    tokenList = []
    count = 0
    while (count < tokens):
        newToken = Token(0, boxList[0])
        boxList[0].tokenList.append(newToken)
        tokenList.append(newToken)
        count += 1
    count = 0
    while (count < timeSteps):
        TokenRules[0](boxList,tokenList)
        boxesRules[0](boxList)
        print(len(boxList))


main()