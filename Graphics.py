from tkinter import *

from Maze import Maze


class Graphics:
    def __init__(self):
        self._window = Tk()
        self._maze = Maze(self)
        self.sizeTiles = 20

    def menuFrame(self):
        def dfs():
            print("DFS algorithm chosen")
            self.clearWindow()
            self.mazeFrame()
            self._maze.mazeToGraph()

        def bfs():
            print("BFS algorithm chosen")
            self.clearWindow()
            self.mazeFrame()

        Label(self._window, text="Select the algorithm you wish to use to solve the labyrinth").pack(side=TOP, padx=5,
                                                                                                     pady=5)
        Button(self._window, text="DFS", command=dfs).pack(side=RIGHT, padx=5, pady=5)
        Button(self._window, text="BFS", command=bfs).pack(side=LEFT, padx=5, pady=5)
        self._window.mainloop()

    def mazeFrame(self):
        maze = self._maze.maze
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 1:
                    Canvas(self._window, bg="black", width=self.sizeTiles, height=self.sizeTiles).grid(column=x, row=y,
                                                                                                       padx=0, pady=0)
                elif maze[y][x] == 2:
                    Canvas(self._window, bg="blue", width=self.sizeTiles, height=self.sizeTiles).grid(column=x, row=y,
                                                                                                      padx=0, pady=0)
                elif maze[y][x] == 3:
                    Canvas(self._window, bg="red", width=self.sizeTiles, height=self.sizeTiles).grid(column=x, row=y,
                                                                                                     padx=0, pady=0)
                else:
                    Canvas(self._window, bg="white", width=self.sizeTiles, height=self.sizeTiles).grid(column=x, row=y,
                                                                                                       padx=0, pady=0)

    def changeTileColor(self, cooX, cooY, color):
        Canvas(self._window, bg=color, width=self.sizeTiles, height=self.sizeTiles).grid(column=cooX, row=cooY,
                                                                                         padx=0, pady=0)

    def changeTileColorWithText(self, cooX, cooY, color, txt):
        canvas = Canvas(self._window, bg=color, width=self.sizeTiles, height=self.sizeTiles)
        canvas.create_text(self.sizeTiles/2, self.sizeTiles/2, text=txt)
        canvas.grid(column=cooX, row=cooY, padx=0, pady=0)

    def clearWindow(self):
        for i in self._window.winfo_children():
            i.destroy()

    @property
    def window(self):
        return self._window
