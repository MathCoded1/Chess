from Game_Board import GameBoard
from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King


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
        self.moves = []

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
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('A', 2)), 'A', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('B', 2)), 'B', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('C', 2)), 'C', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('D', 2)), 'D', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('E', 2)), 'E', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('F', 2)), 'F', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('G', 2)), 'G', 2)
        self.place(Pawn(self.get_player_1(), self.get_board().get_square('H', 2)), 'H', 2)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('A', 7)), 'A', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('B', 7)), 'B', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('C', 7)), 'C', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('D', 7)), 'D', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('E', 7)), 'E', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('F', 7)), 'F', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('G', 7)), 'G', 7)
        self.place(Pawn(self.get_player_2(), self.get_board().get_square('H', 7)), 'H', 7)
        self.place(Rook(self.get_player_1(), self.get_board().get_square('A', 1)), 'A', 1)
        self.place(Rook(self.get_player_1(), self.get_board().get_square('H', 1)), 'H', 1)
        self.place(Rook(self.get_player_2(), self.get_board().get_square('A', 8)), 'A', 8)
        self.place(Rook(self.get_player_2(), self.get_board().get_square('H', 8)), 'H', 8)
        self.place(Knight(self.get_player_1(), self.get_board().get_square('B', 1)), 'B', 1)
        self.place(Knight(self.get_player_1(), self.get_board().get_square('G', 1)), 'G', 1)
        self.place(Knight(self.get_player_2(), self.get_board().get_square('B', 8)), 'B', 8)
        self.place(Knight(self.get_player_2(), self.get_board().get_square('G', 8)), 'G', 8)
        self.place(Bishop(self.get_player_1(), self.get_board().get_square('C', 1)), 'C', 1)
        self.place(Bishop(self.get_player_1(), self.get_board().get_square('F', 1)), 'F', 1)
        self.place(Bishop(self.get_player_2(), self.get_board().get_square('C', 8)), 'C', 8)
        self.place(Bishop(self.get_player_2(), self.get_board().get_square('F', 8)), 'F', 8)
        self.place(Queen(self.get_player_1(), self.get_board().get_square('D', 1)), 'D', 1)
        self.place(Queen(self.get_player_2(), self.get_board().get_square('D', 8)), 'D', 8)
        self.place(King(self.get_player_1(), self.get_board().get_square('E', 1)), 'E', 1)
        self.place(King(self.get_player_2(), self.get_board().get_square('E', 8)), 'E', 8)
