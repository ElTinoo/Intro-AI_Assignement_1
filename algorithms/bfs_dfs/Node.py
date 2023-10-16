class Node:

    def __init__(self, idP, cooXP, cooYP):  # Constructor
        self._id = idP
        self._cooX = cooXP
        self._cooY = cooYP
        self._idNeighbours = []

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
    def idNeighbours(self):
        return self._idNeighbours

    @idNeighbours.setter
    def idNeighbours(self, value):
        self._idNeighbours.append(value)
