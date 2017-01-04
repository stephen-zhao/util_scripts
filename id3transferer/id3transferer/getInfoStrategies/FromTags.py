from id3transferer.getInfoStrategies.GetInfoStrategy import GetInfoStrategy
from id3transferer import SoundInfo


class GetInfoStrategyFromTags(GetInfoStrategy):
    def __init__(self):
        return

    def getInfoImpl(self, file):
        return SoundInfo(
            title="Demo from Tags",
            artist="Newton ft. Illinois",
            album_title="Demonstration",
            album_artist="Newton",
            year="2016",
            track_num="1",
            disc_num="1",
            genre="Alternative Jam",
            composer="Newton and Goulding",
            comment="Does this work?")

    @classmethod
    def getNameAbbr(cls):
        return "tags"
