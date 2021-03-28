from . import Piece
from Move import Move


class Queen(Piece.Piece):
    def __init__(self, player, starting_square):
        super.__init__(player, starting_square)
        self.name = 'QUEEN'


def possible_moves(self):
    moves = []