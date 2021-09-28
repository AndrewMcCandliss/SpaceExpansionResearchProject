class Boxes(object):
    """Describes a box and what it contains"""
    def __init__(self, tokenList):
        self.tokenList = tokenList
    def GetNumTokens(self):
        return len(self.tokenList)

