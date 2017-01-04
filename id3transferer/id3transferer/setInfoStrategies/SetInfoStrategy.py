from id3transferer.exceptions import *


class SetInfoStrategy:
    def __init__(self):
        raise AbstractInstantiationException("SetInfoStrategy")

    def setInfoImpl(self, file, soundInfo):
        raise AbstractMethodCallException("setInfoImpl")

    @classmethod
    def getStratNameAbbr(cls):
        raise AbstractMethodCallException("getStratNameAbbr")

    @classmethod
    def getStratListAbbr(cls):
        return [sub.getNameAbbr()
                for sub in SetInfoStrategy.__subclasses__()]

    @classmethod
    def createStrategy(cls, abbr):
        for sub in SetInfoStrategy.__subclasses__():
            if sub.getNameAbbr() == abbr:
                return sub()
