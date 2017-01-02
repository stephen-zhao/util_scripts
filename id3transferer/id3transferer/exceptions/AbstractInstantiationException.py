class AbstractInstantiationException:
    def __init__(self, cls):
        self._cls = cls
        self._descPre = "Tried to instantiate abstract class"

    def __str__(self):
        return " ".join([self._descPre, self._cls])
