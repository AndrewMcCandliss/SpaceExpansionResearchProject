class Token(object):
    """Defines a token and the consequences of it's movement"""
    
    def __init__(self, pos):
        self.pos = pos
    def move(self, movement, boxesList):
        """This takes a movement in a string, and a list of boxes"""
        if(movement == 'left'):
            if(self.pos == 0):
                boxesList[self.pos].remove(self)
                self.pos = len(boxesList) - 1
                boxesList[self.pos].append(self)
            else:
                boxesList[self.pos].remove(self)
                self.pos -= 1
                boxesList[self.pos].append(self)
        if(movement == 'right'):
            if(self.pos == len(boxesList) - 1):
                boxesList[self.pos].remove(self)
                self.pos = 0
                boxesList[self.pos].append(self)
            else:
                boxesList[self.pos].remove(self)
                self.pos += 1
                boxesList[self.pos].append(self)
