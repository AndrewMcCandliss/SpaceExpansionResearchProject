class Token(object):
    """Defines a token and the consequences of it's movement"""
    
    def __init__(self, pos, box):
        self.pos = pos
        self.box = box
    def move(self, movement, boxesList):
        """This takes a movement in a string, and a list of boxes"""
        if(movement == 'left'):
            if(self.pos == 0):
                self.box.tokenList.remove(self)
                self.box = boxesList[-1]
                self.pos = len(boxesList) - 1
                self.box.tokenList.append(self)
            else:
                self.box.tokenList.remove(self)
                self.pos -= 1
                self.box = boxesList[self.pos]
                self.box.tokenList.append(self)
        if(movement == 'right'):
            if(self.pos == len(boxesList) - 1):
                self.box.tokenList.remove(self)
                self.pos = 0
                self.box = boxesList[self.pos]
                self.box.tokenList.append(self)
            else:
                self.box.tokenList.remove(self)
                self.pos += 1
                self.box = boxesList[self.pos]
                self.box.tokenList.append(self)
