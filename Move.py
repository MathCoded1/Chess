

class Move:
    number = None
    from_square = None
    to_square = None
    piece_type = None
    capture = None

    def __init__(self, piece_type, from_square,  to_square):
        super.__init__()
        self.piece_type = piece_type
        self.from_square = from_square
        self.to_square = to_square
