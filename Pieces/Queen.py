import Pieces.Piece as Piece
import Move.move as Move

class Queen(Piece):
    def __init__(self, player):
        super.__init__()
        self.name = 'PAWN'
        self.player = player
        self.board = self.player.get_board()
        self.color =  self.player.get_color()
        self.alive = 'TRUE'
        self.number_of_moves = 0
def possible_moves(self):
    moves = list(Move)
