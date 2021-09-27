from Token import Token
from random import Random

def TokenMovementAttraction(boxesList, TokenList):
    for token in TokenList:
        lC = boxesList[token.pos - 1].GetNumTokens() + 1
        rC
        if (token.pos == len(boxesList) - 1):
            rC = boxesList[0].GetNumTokens() + 1
        else:
            rC = boxesList[token.pos + 1].GetNumTokens() + 1
        cC = boxesList[token.pos].GetNumTokens() + 1
        lChance = (lC * 100 ) / (lC + rC + cC)
        rChance = (rC * 100 ) / (lC + rC + cC)
        cChance = (cC * 100 ) / (lC + rC + cC)
        d100 = Random.randint(1,100)
        if(d100 <= lChance):
            token.move('left', boxesList)
            print('token moves left')
        elif(d100 > 100 - rChance):
            token.move('right', boxesList)
            print('token moves right')
        else:
            print("token doesn't move")

def BoxesChangingSplitting(BoxesList):
    i = 0
    while (i < len(BoxesList)):

