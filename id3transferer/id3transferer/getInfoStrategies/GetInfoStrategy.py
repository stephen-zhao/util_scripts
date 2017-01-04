from ..exceptions import *


class GetInfoStrategy:
    def __init__(self):
        raise AbstractInstantiationException("GetInfoStrategy")

    def getInfoImpl(self, file):
        raise AbstractMethodCallException("getInfoImpl")

    @classmethod
    def getStratNameAbbr(cls):
        raise AbstractMethodCallException("getStratNameAbbr")

    @classmethod
    def getStratListAbbr(cls):
        print(vars())
        return [sub.getNameAbbr()
                for sub in GetInfoStrategy.__subclasses__()]

    @classmethod
    def createStrategy(cls, abbr):
        for sub in GetInfoStrategy.__subclasses__():
            if sub.getNameAbbr() == abbr:
                return sub()
