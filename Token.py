class Token(object):
    """Defines a token and the consequences of it's movement"""
    
    def __init__(self, box):
        self.box = box
    def pos(self, boxesList)
        return self.box.GetPos(boxesList)
    def move(self, movement, boxesList):
        """This takes a movement in a string, and a list of boxes"""
        if(movement == 'left'):
            if(self.pos(boxesList) == 0):
                self.box.tokenList.remove(self)
                self.box = boxesList[-1]
                self.box.tokenList.append(self)
            else:
                self.box.tokenList.remove(self)
                self.box = boxesList[self.pos(boxesList) - 1]
                self.box.tokenList.append(self)
        if(movement == 'right'):
            if(self.pos(boxesList) == len(boxesList) - 1):
                self.box.tokenList.remove(self)
                self.box = boxesList[0]
                self.box.tokenList.append(self)
            else:
                self.box.tokenList.remove(self)
                self.box = boxesList[self.pos(boxesList) + 1]
                self.box.tokenList.append(self)
