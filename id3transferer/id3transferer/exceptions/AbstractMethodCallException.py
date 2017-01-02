class AbstractMethodCallException:
    def __init__(self, mtd):
        self._mtd = mtd
        self._descPre = "Tried to call abstract method"
        self._descSuf = "(...)"

    def __str__(self):
        return " ".join([self._descPre, self._mtd, self._descSuf])
