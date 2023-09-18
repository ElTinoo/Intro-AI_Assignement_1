import tkinter.messagebox
from tkinter import *
from Maze import Maze
from algorithms.BFS import BFS
from algorithms.DFS import DFS


class Graphics:
    def __init__(self):
        self._window = Tk()
        self._frameMaze = None
        self._frame2 = None
        self._maze = Maze(self)
        self.sizeTiles = 20

    def menuFrame(self):  # I've started to plan the possibility to import an external maze
        def defaultMaze():  # function linked to the default maze button
            self.clearWindow()
            self.mazeFrame()  # we construct the representation of the maze (Maze.defaultMaze())
            self._maze.mazeToGraph()

        def importMaze():
            pass

        # Ask if we want to import an external maze
        Label(self._window, text="Do you want to use the default maze or import one ?").pack(side=TOP, padx=5, pady=5)
        Button(self._window, text="default maze", command=defaultMaze).pack(side=RIGHT, padx=5, pady=5)
        Button(self._window, text="import", command=importMaze).pack(side=LEFT, padx=5, pady=5)
        self._window.mainloop()

    def mazeFrame(self):  # on my window I add two frame, one for the maze and the other one for the buttons
        # ---------- Frame that contains the Maze ----------
        self._frameMaze = Frame(self._window)
        maze = self._maze.maze

        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 1:  # if we have a wall -> black color
                    Canvas(self._frameMaze, bg="black", width=self.sizeTiles, height=self.sizeTiles).grid(
                        column=x, row=y, padx=0, pady=0)
                elif maze[y][x] == 2:  # if we have the starting cell -> blue color
                    Canvas(self._frameMaze, bg="blue", width=self.sizeTiles, height=self.sizeTiles).grid(
                        column=x, row=y, padx=0, pady=0)
                elif maze[y][x] == 3:  # if we have the end cell -> black color
                    Canvas(self._frameMaze, bg="red", width=self.sizeTiles, height=self.sizeTiles).grid(
                        column=x, row=y, padx=0, pady=0)
                else:  # else it means that we have nothing on the cell -> white color
                    Canvas(self._frameMaze, bg="white", width=self.sizeTiles, height=self.sizeTiles).grid(
                        column=x, row=y, padx=0, pady=0)
        self._frameMaze.pack(side=LEFT)

        # ---------- Frame that contains the others windget ----------
        def dfsFunction():  # function linked to the dfs maze button
            dfs = DFS(self._maze.nodeList, self._maze.startNodeId, self._maze.endNodeId)
            if dfs.verifyPath():
                labelTime.config(text=f"Time to solve : {dfs.timeToSolve}s")
            else:
                tkinter.messagebox.showwarning('Hmm mm', 'No path found ! The maze hase no solution')

        def bfsFunction():  # function linked to the bfd maze button
            bfs = BFS(self._maze.nodeList, self._maze.startNodeId, self._maze.endNodeId)
            if bfs.verifyPath():
                labelTime.config(text=f"Time to solve : {bfs.timeToSolve}s")
            else:
                tkinter.messagebox.showwarning('Hmm mm', 'No path found ! The maze hase no solution')

        self._frame2 = Frame(self._window)
        Label(self._frame2, text="Chose the algorythm to start").pack()
        Button(self._frame2, text="BFS", command=bfsFunction).pack(side=LEFT)
        Button(self._frame2, text="DFS", command=dfsFunction).pack(side=RIGHT)
        labelTime = Label(self._frame2, text="Time to solve :")
        labelTime.pack()
        self._frame2.pack(side=RIGHT)

    def changeTileColor(self, cooX, cooY, color):
        # function that allow to other classes to change the color of a specific cell
        Canvas(self._frameMaze, bg=color, width=self.sizeTiles, height=self.sizeTiles).grid(column=cooX, row=cooY,
                                                                                            padx=0, pady=0)

    def changeTileColorWithText(self, cooX, cooY, color, txt):
        # function that allow to other classes to change the color and add a text of a specific cell
        canvas = Canvas(self._frameMaze, bg=color, width=self.sizeTiles, height=self.sizeTiles)
        canvas.create_text(self.sizeTiles / 2, self.sizeTiles / 2, text=txt)
        canvas.grid(column=cooX, row=cooY, padx=0, pady=0)

    def clearWindow(self):  # clear all the widgets existing in the window
        for i in self._window.winfo_children():
            i.destroy()

    @property
    def window(self):
        return self._window
