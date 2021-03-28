from . import Piece
from Move import Move


class Queen(Piece.Piece):
    def __init__(self, player):
        self.name = 'PAWN'
        self.player = player
        self.board = self.player.get_board()
        self.color = self.player.get_color()
        self.alive = 'TRUE'
        self.number_of_moves = 0


def possible_moves(self):
    moves = []