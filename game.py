from tkinter import *
from maze import Maze
from pacman import Pacman

m = Maze()
m.initialize_maze()
m.draw_maze()
m.root.mainloop()