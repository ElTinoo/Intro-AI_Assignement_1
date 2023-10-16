import time


class DFS:
    def __init__(self, graphP, startIdNodeIdP, endNodeIdP):
        # Initialization of the DFS class with the graph, start node, and end node
        self._graph = graphP
        self._startNodeId = startIdNodeIdP
        self._endNodeId = endNodeIdP
        self._path = []  # List to store the found path
        self._timeToSolve = -1  # Time taken to solve the problem
        self.run()  # Calls the run method to solve the problem

    def run(self):
        startTime = time.time()  # Records the time at the beginning of execution
        parentList = self.solveMaze()  # Calls the solveMaze method to find the path
        self._path = self.reconstructPath(parentList)  # Reconstructs the path from the parent list
        self._timeToSolve = time.time() - startTime  # Calculates the total time to solve the problem

    def solveMaze(self):
        # /!\ -------------- /!\
        # a DFS plunge depth first into a graph without regrade for wich edge it take next until it cannot go
        # any further at which point it backtracks and continue
        # I've used the same method as the BFS to reconstruct the path. refer to the line 11 of the BFS class
        # /!\ -------------- /!\

        visitedNode = [False] * len(self._graph)  # List to track visited nodes
        parentList = [-1] * len(self._graph)  # List to store parents of each node

        def dfs(node):
            if visitedNode[node.id]:
                pass  # If the node has already been visited -> do nothing
            else:
                visitedNode[node.id] = True  # Marks the node as visited
                for child in node.idNeighbours:  # Iterates through the node's neighbors
                    if not visitedNode[child]:
                        parentList[child] = node.id  # Stores the current node as the parent
                    dfs(self._graph[child])  # Calls the dfs function recursively for neighbors

        dfs(self._graph[self._startNodeId])
        return parentList

    def reconstructPath(self, parentList):
        path = []
        parent = self._endNodeId

        while parent != -1:
            path.append(parent)  # Adds the current node to the path
            parent = parentList[parent]  # Moves to the next parent

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
