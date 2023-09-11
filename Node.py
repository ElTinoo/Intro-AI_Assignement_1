class Node:

    def __init__(self, idP, cooXP, cooYP):  # Constructor
        self._id = idP
        self._cooX = cooXP
        self._cooY = cooYP
        self._idNeighbour = []

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
    def idNeighbour(self):
        return self._idNeighbour

    @idNeighbour.setter
    def idNeighbour(self, value):
        self._idNeighbour.append(value)
