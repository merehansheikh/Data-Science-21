class CityData:

    def __init__(self, index, name, outConCount, outCons):
        self.index = index
        self.name = name
        self.outConCount = outConCount
        self.outCons = outCons
        self.seen = False
        self.predecessor = -1

    def set_seen(self):

        self.seen = True

    def set_predecessor(self, ind):

        self.predecessor = ind
