class Tile:
    def __init__(self, idP, cooX, cooY, score, role):
        self._id = idP
        self._cooX = cooX
        self._cooY = cooY
        self._tileScore = score  # 1 -> void | 1000 -> wall
        self._role = role  # O -> void | 1 -> wall | 2 -> start | 3 -> end

    @property
    def id(self):
        return self._id

    @property
    def cooX(self):
        return self._cooX

    @property
    def cooY(self):
        return self._cooY

    @property
    def tileScore(self):
        return self._tileScore
