from Move import Move


class Piece(object):

    name = None
    player = None
    color = None
    alive = None
    value = None
    square = None
    board = None
    moves = None
    number_of_moves = None

    def __init__(self, player, starting_square):
        self.name = None
        self.player = player
        self.board = self.player.get_board()
        self.color = self.player.get_color()
        self.alive = 'TRUE'
        self.square = starting_square
        self.moves = []
        self.number_of_moves = 0

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def is_alive(self):
        return self.alive

    def set_alive(self, is_alive):
        self.alive = is_alive

    def kill(self):
        self.alive = False

    def possible_moves(self):
        pass

    def valid_moves(self):
        pass

    def get_square(self):
        return self.square

    def is_color_1(self):
        if self.get_square().get_grid().get_host().is_color_1():
            return True
        else:
            return False

    def is_color_2(self):
        if self.get_board().is_color_2():
            return True
        else:
            return False

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_moves(self):
        return self.moves

    def set_moves(self, moves):
        self.moves = moves