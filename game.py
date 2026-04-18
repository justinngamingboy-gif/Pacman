from tkinter import *
from maze import Maze
from pacman import Pacman

root = Tk()
canvas = Canvas(root, width=600, height=550, bg="black")
canvas.pack()

m = Maze(canvas)
m.draw_maze()

root.mainloop()