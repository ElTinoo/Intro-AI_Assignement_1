from graphics.Graphics import Graphics

if __name__ == '__main__':
    graphics = Graphics()
    graphics.menuFrame()  # we start the program

# The program begins by graphically initializing the representation of the labyrinth using the Graphics.py class.

# Then, starting from the labyrinth, we create the graph associated with it. To do this, I start by placing nodes
# only where they're needed, to save processing time and memory, and then connect them together.

# Each node created is stored in an array indexed by the node identifier. This makes it possible to retrieve the node
# sought by its identifier as quickly as possible.

# The Node.py class has 4 attributes: its identifier, its X and Y position in the maze and a list of its neighbors.
