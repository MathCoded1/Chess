from Piece import Piece
from Move import Move


class Rook(Piece):
    def __init__(self, player):
        super.__init__()
        self.name = 'ROOK'
        self.player = player
        self.board = self.player.get_board()
        self.color = self.player.get_color()
        self.alive = 'TRUE'
        self.number_of_moves = 0

    def possible_move(self):
        moves_list = list()

        moves_list.append(self.get_board().all)
