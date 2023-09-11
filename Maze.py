from Node import Node


def defaultMaze():
    return [  # 1-->wall, 0-->void, 2-->start, 3-->end
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
         0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
         1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0,
         1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0,
         0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1,
         1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
         1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
         0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0,
         1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
         1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1,
         1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3,
         0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1]
    ]


class Maze:
    def __init__(self, graphicsP):
        self.graphics = graphicsP
        self._maze = defaultMaze()
        self._nodeList = []
        self._graph = None
        self._idNode = 0

    def mazeToGraph(self):
        print("----------- creating the graph -----------")

        # Create and place all the nodes
        print("creating the nodes...")

        def createNode(cooXP, cooYP, changeColor):
            if changeColor:
                self.graphics.changeTileColorWithText(cooXP, cooYP, "green", self._idNode)
                self._nodeList.append(Node(self._idNode, cooXP, cooYP))
            else:
                self._nodeList.append(Node(self._idNode, cooXP, cooYP))
            self._idNode += 1

        for y in range(len(self._maze)):
            for x in range(len(self._maze[y])):
                if self._maze[y][x] == 2 or self._maze[y][x] == 3:  # if it's the starting point or the end point
                    createNode(x, y, False)

                elif self._maze[y][x] == 0:  # if we are on a blank tile

                    # if wall right & below
                    if self._maze[y][x + 1] == 1 and self._maze[y + 1][x] == 1:
                        createNode(x, y, True)

                    # if wall left & void right
                    elif self._maze[y][x - 1] == 1 and self._maze[y][x + 1] == 0:
                        createNode(x, y, True)

                    # if left & below void & right wall
                    elif self._maze[y][x - 1] == 0 and self._maze[y][x + 1] == 1 and self._maze[y + 1][x] == 0:
                        createNode(x, y, True)

                    # if wall left & right & top
                    elif self._maze[y][x - 1] == 1 and self._maze[y][x + 1] == 1 and self._maze[y - 1][x] == 1:
                        createNode(x, y, True)

                    elif self._maze[y][x + 1] == 0 and self._maze[y][x - 1] == 0:  # if void right & left
                        if self._maze[y - 1][x] == 0 or self._maze[y + 1][x] == 0:  # if void top or below
                            createNode(x, y, True)

        # Connect all the nodes together
        print("connecting all the nodes...")
        for node in self._nodeList:

            # if there is no wall to the left, add the id of the node to its left
            if self._maze[node.cooY][node.cooX - 1] == 0:
                node.idNeighbour.append(node.id - 1)

            # if there is no wall to the right, add the id of the node to its right
            if self._maze[node.cooY][node.cooX + 1] == 0:
                node.idNeighbour.append(node.id + 1)

            # if there is no wall to the top, add the id of the node to its top
            if self._maze[node.cooY - 1][node.cooX] == 0:
                # as long as we don't come across a node with a lower Y and the same X coordinate as the current one.
                i = node.id - 1  # we know that the node above us have a lower id than the current node
                while self.nodeList[i].cooX != node.cooX:
                    i -= 1
                node.idNeighbour.append(i)

            # if there is no wall below, add the id of the node below
            if self._maze[node.cooY + 1][node.cooX] == 0:
                # as long as we don't come across a node with a higher Y and the same X coordinate as the current one.
                i = node.id + 1  # we know that the node above us have an upper id than the current node
                while self.nodeList[i].cooX != node.cooX:
                    i += 1
                node.idNeighbour.append(i)

    @property
    def graph(self):
        return self._graph

    @property
    def nodeList(self):
        return self._nodeList

    @property
    def mazeLength(self):
        return len(self._maze)

    @property
    def mazeWidth(self):
        return len(self._maze[0])

    @property
    def maze(self):
        return self._maze
