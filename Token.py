class Token(object):
    """Defines a token and the consequences of it's movement"""
    
    def __init__(self, pos, box):
        self.pos = pos
        self.box = box
    def move(self, movement, boxesList):
        """This takes a movement in a string, and a list of boxes"""
        if(movement == 'left'):
            if(pos == 0):
                box.remove(self)
                box = boxesList[-1]
                pos = len(boxesList) - 1
                box.append(self)
            else:
                box.remove(self)
                pos -= 1
                box = boxesList[pos]
                box.append(self)
        if(movement == 'right'):
            if(pos == len(boxesList) - 1):
                boxesList[pos] -= 1
                pos = 0
                boxesList[pos] += 1
            else:
                boxesList[pos] -= 1
                pos =+ 1
                boxesList[pos] += 1
