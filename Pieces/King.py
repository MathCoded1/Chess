from . import Piece
from Move import Move


class King(Piece.Piece):
    def __init__(self, player, starting_square):
        super().__init__(player, starting_square)
        self.name = 'KING'

    def possible_moves(self):
        moves_list = [Move(self.get_board().forward(self.get_square())), Move(self.get_board().back(self.get_square())),
                      Move(self.get_board().right(self.get_square())), Move(self.get_board().left(self.get_square())),
                      Move(self.get_board().forward_left(self.get_square())),
                      Move(self.get_board().forward_right(self.get_square())),
                      Move(self.get_board().back_left(self.get_square())),
                      Move(self.get_board().back_right(self.get_square()))]
        return moves_list
