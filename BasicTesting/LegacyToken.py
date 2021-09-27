from random import Random
class Token(object):
    """Defines a Token and How it moves"""
    
    def __init__(self, pos):
        self.pos = pos
    def move(self, rL, rR, boxesList):
        Random().seed()
        chance = Random().randint(1, 100)
        if(chance <= rL):
            boxesList[self.pos] -= 1
            if(self.pos == 0):
                boxesList[-1] += 1
                self.pos = len(boxesList) - 1
            else:
                boxesList[self.pos - 1] += 1
                self.pos -= 1
            

        elif(chance >= 100 - rR):
            boxesList[self.pos] -= 1
            if(self.pos == len(boxesList) - 1):
                boxesList[0] += 1
                self.pos = 0
            else:
                boxesList[self.pos + 1] += 1
                self.pos += 1


