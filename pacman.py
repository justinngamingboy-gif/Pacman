class Pacman:
    def __init__(self, canvas, row, col):
        self.cell_size = 25
        self.canvas = canvas
        self.row = row
        self.col = col
        self.id = None

    def draw_pacman(self):
        x1 = self.col * self.cell_size
        y1 = self.row * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        self.id = self.canvas.create_oval(
            x1, y1, x2, y2,
            fill="yellow",
            outline="yellow"
        )