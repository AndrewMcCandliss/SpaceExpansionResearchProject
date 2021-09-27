
from Token import Token
from random import Random

def main():
    amntOfBoxes = 1
    amntOfTokens = 400
    rL = 40
    rR = 40
    iterations = 100
    tokens = []
    boxes = [0]
    count = 0
    SpreadTokens(boxes, tokens, amntOfTokens, amntOfBoxes)
    while(count < iterations):
        count += 1
        for token in tokens:
            token.move(rL, rR, boxes)
        print(boxes)
        boxes.extend([0,0])

def CreateBoxes(amntOfBoxes, boxesList):
    count = 0
    while(count < amntOfBoxes):
        count += 1
        boxesList.append(0)

def SpreadTokens(boxesList, tokens, amntOfTokens, amntOfBoxes):
    count = 0
    while(count < amntOfTokens):
        count += 1
        rndNum = Random().randint(0, amntOfBoxes - 1)
        newtoken = Token(rndNum)
        tokens.append(newtoken)
        boxesList[rndNum] += 1


main()

# visualization
# Animation of population over time
# Entropy and Max Entropy over time + gap between them

# Potential Rules
# boxes can split/merge based on population
# tokens chance of moving can change based on population
