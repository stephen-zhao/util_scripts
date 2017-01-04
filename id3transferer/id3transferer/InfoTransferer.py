class InfoTransferer:
    def __init__(self, getInfoStrategy, setInfoStrategy):
        self.getInfoStrategy = getInfoStrategy
        self.setInfoStrategy = setInfoStrategy

    def getInfo(self, file):
        return self.getInfoStrategy.getInfoImpl(file)

    def setInfo(self, file, soundInfo):
        self.setInfoStrategy.setInfoImpl(file, soundInfo)

    def transfer(self, file):
        self.setInfo(file, self.getInfo(file))
