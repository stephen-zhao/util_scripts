from .. import exceptions


class GetInfoStrategy:
    def __init__(self):
        raise exceptions.AbstractInstantiationException("GetInfoStrategy")

    def getNameAbbr(self):
        raise exceptions.AbstractMethodCallException("getNameAbbr")

    def getInfoImpl(self, file):
        raise exceptions.AbstractMethodCallException("getInfoImpl")

    @classmethod
    def getStratListAbbr(cls):
        return [sub.getNameAbbr()
                for sub in vars()["GetInfoStrategy"].__subclasses__()]

    @classmethod
    def createStrategy(cls, abbr):
        for sub in vars()["GetInfoStrategy"].__subclasses__():
            if sub.getNameAbbr() == abbr:
                return sub()
