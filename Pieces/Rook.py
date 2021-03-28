from . import Piece
from Move import Move


class Rook(Piece.Piece):
    def __init__(self, player, starting_square):
        super().__init__(player, starting_square)
        self.name = 'ROOK'

    def possible_move(self):
        moves_list = list()

        moves_list.append(self.get_board().all)
