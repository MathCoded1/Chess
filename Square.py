import Pieces.Piece as Piece


class Square:
    name = 'SQUARE'
    grid = None
    x = None
    y = None
    color = None
    occupant = None

    def __init__(self):
        super()

    def __init__(self, grid, x, y, color, occupant):
        super()
        self.grid = grid
        self.x = x
        self.y = y
        self.color = color
        self.occupant = occupant

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_occupant(self):
        return self.occupant

    def set_occupant(self, occupant):
        self.occupant = occupant
        self.get_occupant().set_square(self)

