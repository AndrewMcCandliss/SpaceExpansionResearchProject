class Token(object):
    """Defines a token and the consequences of it's movement"""
    
    def __init__(self, pos):
        self.pos = pos
    def move(self, movement, boxesList):
        """This takes a movement in a string, and a list of boxes"""
        if(movement == 'left'):
            if(pos == 0):
                boxesList[0] -= 1
                pos = Len(boxesList) - 1
                boxesList[pos] += 1
            else:
                boxesList[pos] -= 1
                pos -= 1
                boxesList[pos] += 1
        if(movement == 'right'):
            if(pos == len(boxesList) - 1):
                boxesList[pos] -= 1
                pos = 0
                boxesList[pos] += 1
            else:
                boxesList[pos] -= 1
                pos =+ 1
                boxesList[pos] += 1

