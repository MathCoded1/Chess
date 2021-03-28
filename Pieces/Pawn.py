from . import Piece
from Move import Move


class Pawn(Piece.Piece):

    def __init__(self, player, starting_square):
        super().__init__(player, starting_square)
        self.name = 'PAWN'

    def possible_moves(self):
        moves = []
        if len(self.get_moves()) != 0:
            if self.is_color_1():
                moves.append(self.get_board().forward(self.get_board().forward(self.get_square())))
            else:
                moves.append(self.get_board().back(self.get_board().back(self.get_square())))
        else:
            if self.is_color_1():
                moves.append(self.get_board().forward(self.get_square()))
            else:
                moves.append(self.get_board().back(self.get_square()))
        if self.get_board().forward_left(self.get_square()) is not None:
            square = self.get_board().forward_left(self.get_square())
            if square.get_occupant() is not None:
                if square.get_occupant().get_color() is not self.get_color():
                    moves.append(square)
        if self.get_board().forward_right(self.get_square()) is not None:
            square = self.get_board().forward_right(self.get_square())
            if square.get_occupant() is not None:
                if square.get_occupant().get_color() is not self.get_color():
                    moves.append(square)
        return moves

    def valid_moves(self):
        possible_moves = self.possibile_moves()
        moves = []








