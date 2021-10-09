class Boxes(object):
    """Describes a box and what it contains"""
    def __init__(self, tokenList):
        self.tokenList = tokenList
    def GetNumTokens(self):
        """Returns the amount of tokens attached to the box"""
        return len(self.tokenList)
    def GetPos(self, boxesList):
        """Finds the position of the box in the box list"""
        return boxesList.index(self)
        
