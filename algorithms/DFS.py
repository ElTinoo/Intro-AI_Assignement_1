import time


class DFS:
    def __init__(self, graphP, startIdNodeIdP, endNodeIdP):
        self._graph = graphP
        self._startNodeId = startIdNodeIdP
        self._endNodeId = endNodeIdP
        self._path = []
        self._timeToSolve = -1
        self.run()

    def run(self):
        startTime = time.time()
        parentList = self.solveMaze()
        self._path = self.reconstructPath(parentList)
        self._timeToSolve = time.time() - startTime

    def solveMaze(self):
        visitedNode = [False] * len(self._graph)
        parentList = [-1] * len(self._graph)

        def dfs(node):
            if visitedNode[node.id]:
                pass
            else:
                visitedNode[node.id] = True
                for child in node.idNeighbours:
                    if not visitedNode[child]:
                        parentList[child] = node.id
                    dfs(self._graph[child])

        dfs(self._graph[0])
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
        return self.path
