import Square as Square


class Grid(object):
    squares = None
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    host = None

    def __init__(self):
        super.__init__()
        self.name = 'GRID'

    def __init__(self, min_x, max_x, min_y, max_y):
        super()
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        #self.squares = Square([self.max_x-self.min_x][self.max_y-self.min_y])

    def get_square_by_square(self, square_to_find):
        for square in self.squares:
            if square.get_y() is square_to_find.get_y() and square.get_x() is square_to_find.get_x():
                return square
            else:
                return None

    def get_x_y(self, x_to_find, y_to_find):
        for square in self.squares:
            if square.get_y() is y_to_find and square.get_x() is x_to_find:
                return square

    def square_up(self, x, y):
        if y < self.max_y:
            return self.get_x_y(x, y+1)
        else:
            return None

    def square_down(self, x, y):
        if y > self.min_y:
            return self.get_x_y(x, y-1)
        else:
            return None

    def square_right(self, x, y):
        if x < self.max_x:
            return self.get_x_y(x+1, y)
        else:
            return None

    def square_left(self, x, y):
        if x > self.min_x:
            return self.get_x_y(x-1, y)
        else:
            return None

    def square_up_right(self, x, y):
        if x < self.max_x and y < self.max_y:
            return self.get_x_y(x+1, y+1)
        else:
            return None

    def square_up_left(self, x, y):
        if x > self.min_x and y < self.max_y:
            return self.get_x_y(x-1, y+1)
        else:
            return None

    def square_down_right(self, x, y):
        if x < self.max_x and y > self.min_y:
            return self.get_x_y(x+1, y-1)
        else:
            return None

    def square_down_left(self, x, y):
        if x > self.min_x and y > self.min_y:
            return self.get_x_y(x-1, y-1)
        else:
            return None

    def load_squares(self, squares):
        for square in squares:
            self.squares.put(square)

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host

    #def put(self, squares):


