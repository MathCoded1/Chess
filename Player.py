class Player:
    name = None
    board = None
    pieces = None
    game = None

    def __init__(self, board):
        self.board = board

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_pieces(self):
        return self.pieces

    def set_pieces(self, pieces):
        self.pieces = pieces

    def get_game(self):
        return self.game

    def set_game(self, game):
        self.game = game