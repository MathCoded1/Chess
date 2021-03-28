from Game_Board import GameBoard
from Pieces.Pawn import Pawn
import Pieces.Rook as Rook
import Pieces.Knight as Knight
import Pieces.Bishop as Bishop
import Pieces.Queen as Queen
import Pieces.King as King


class Chess:
    board = None
    rules = None
    player_1 = None
    player_2 = None
    moves = None

    def __init__(self, rules, player_1, player_2):
        super()
        self.rules = rules
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = GameBoard(self.rules.color_1,  self.rules.color_2)
        self.moves = list()

    def get_board(self):
        return self.board

    def get_player_1(self):
        return self.player_1

    def get_player_2(self):
        return self.player_2

    def set_board(self, board):
        self.board = board

    def place(self, piece, x,  y):
        self.get_board().place(piece, self.get_board().get_square(x, y))

    def set_up_game(self):
        self.place(Pawn(self.get_player_1()), 'A', 2)
        self.place(Pawn(self.get_player_1()), 'B', 2)
        self.place(Pawn(self.get_player_1()), 'C', 2)
        self.place(Pawn(self.get_player_1()), 'D', 2)
        self.place(Pawn(self.get_player_1()), 'E', 2)
        self.place(Pawn(self.get_player_1()), 'F', 2)
        self.place(Pawn(self.get_player_1()), 'G', 2)
        self.place(Pawn(self.get_player_1()), 'H', 2)
        self.place(Pawn(self.get_player_2()), 'A', 7)
        self.place(Pawn(self.get_player_2()), 'B', 7)
        self.place(Pawn(self.get_player_2()), 'C', 7)
        self.place(Pawn(self.get_player_2()), 'D', 7)
        self.place(Pawn(self.get_player_2()), 'E', 7)
        self.place(Pawn(self.get_player_2()), 'F', 7)
        self.place(Pawn(self.get_player_2()), 'G', 7)
        self.place(Pawn(self.get_player_2()), 'H', 7)
        self.place(Rook(self.get_player_1()), 'A', 1)
        self.place(Rook(self.get_player_1()), 'H', 1)
        self.place(Rook(self.get_player_2()), 'A', 8)
        self.place(Rook(self.get_player_2()), 'H', 8)
        self.place(Knight(self.get_player_1()), 'B', 1)
        self.place(Knight(self.get_player_1()), 'G', 1)
        self.place(Knight(self.get_player_2()), 'B', 8)
        self.place(Knight(self.get_player_2()), 'G', 8)
        self.place(Bishop(self.get_player_1()), 'C', 1)
        self.place(Bishop(self.get_player_1()), 'F', 1)
        self.place(Bishop(self.get_player_2()), 'C', 8)
        self.place(Bishop(self.get_player_2()), 'F', 8)
        self.place(Queen(self.get_player_1()), 'D', 1)
        self.place(Queen(self.get_player_2()), 'D', 8)
        self.place(King(self.get_player_1()), 'E', 1)
        self.place(King(self.get_player_2()), 'E', 8)