from .. import exceptions


class SetInfoStrategy:
    def __init__(self):
        raise exceptions.AbstractInstantiationException("SetInfoStrategy")

    def getNameAbbr(self):
        raise exceptions.AbstractMethodCallException("getNameAbbr")

    def setInfoImpl(self, file, soundInfo):
        raise exceptions.AbstractMethodCallException("setInfoImpl")

    @classmethod
    def getStratListAbbr(cls):
        return [sub.getNameAbbr()
                for sub in vars()["SetInfoStrategy"].__subclasses__()]

    @classmethod
    def createStrategy(cls, abbr):
        for sub in vars()["SetInfoStrategy"].__subclasses__():
            if sub.getNameAbbr() == abbr:
                return sub()
