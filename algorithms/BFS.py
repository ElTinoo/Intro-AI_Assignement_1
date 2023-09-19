import time


class BFS:
    def __init__(self, graphP, startIdNodeIdP, endNodeIdP):
        # Initialization of the BFS class with the graph, start node, and end node
        self._graph = graphP
        self._startNodeId = startIdNodeIdP
        self._endNodeId = endNodeIdP
        self._path = []
        self._timeToSolve = -1
        self.run()

    def run(self):
        # ********************
        # The objective of solving the maze is to return a list that describe the parent of each node (parentList)
        # After that we reconstruct the path from the end node to the start node to find a path
        # ********************
        startTime = time.time()
        parentList = self.solveMaze()
        self._path = self.reconstructPath(parentList)
        self._timeToSolve = time.time() - startTime

    def solveMaze(self):
        # /!\ -------------- /!\
        # A BFS starts at some arbitrary node of a graph and explores the neighbour nodes first before moving to the
        # next neighbours. We add these neighbours to a queue if there are not visited yet. That allows us to visit
        # all the nodes of the maze.
        # As said before our objective is : (go to line 11)
        # /!\ -------------- /!\

        def addNeighbourInLifo(nodeP):
            # here we add the neighbour(s) (child(s)) of the current node (parent) to the fifo and save the relation
            # between parent and child with the parentList[]
            for neighbour in nodeP.idNeighbours:
                if visitedNode[neighbour]:  # if the neighbour has already been visited -> do nothing
                    pass
                else:
                    fifo.append(self._graph[neighbour])  # we add the neighbour in the lifo to visit it later
                    parentList[neighbour] = nodeP.id  # add at the child positionId the id of the parent
            visitedNode[nodeP.id] = True  # we add the current node as visited

        fifo = []  # fifo = first in first out
        visitedNode = [False] * len(self._graph)  # we store the visited node here
        parentList = [-1] * len(self._graph)  # contain -> parentList[child] = parent

        fifo.append(self._graph[0])  # we start at some arbitrary node

        while fifo:  # while we have a node in the queue
            node = fifo[0]
            addNeighbourInLifo(node)
            fifo.remove(node)  # we remove the current node visited from the fifo

        return parentList

    def reconstructPath(self, parentList):
        path = []
        parent = self._endNodeId

        while parent != -1:
            path.append(parent)
            parent = parentList[parent]

        path.reverse()  # we reverse because we have started to reconstruct the path from the end node
        print(path)
        return path

    def verifyPath(self):  # we verify if a path between the start node en the end node exist
        if self._path[0] == self._startNodeId:
            return True
        else:
            return False

    @property
    def timeToSolve(self):
        return self._timeToSolve

    @property
    def path(self):
        return self._path
