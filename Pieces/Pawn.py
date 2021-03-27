import Pieces.Piece as Piece
import Square as Square
import Move.move as Move

class Pawn(Piece):

    possible_moves = None
    possible_attacks = None

    number_of_moves = None

    def __init__(self, player):
        super.__init__()
        self.name = 'PAWN'
        self.player = player
        self.board = self.player.get_board()
        self.color = self.player.get_color()
        self.alive = 'TRUE'
        self.number_of_moves = 0

    def possible_moves(self):
        moves = list(Move)
        if len(self.get_moves()) is not 0:
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
        moves= list(Move)








