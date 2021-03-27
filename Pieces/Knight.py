import Pieces.Piece as Piece
import Move.Move as Move

class Knight(Piece.Piece):

    def possible_moves(self):
        moves_list = list(Move)
        temp_square = self.get_board().forward(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().forward(temp_square)
            if temp_square is not None:
                moves_list.append(self.get_board().left(temp_square))
                moves_list.append(self.get_board().right(temp_square))
        temp_square = self.get_board().back(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().back(temp_square)
            if temp_square is not None:
                moves_list.append(self.get_board().left(temp_square))
                moves_list.append(self.get_board().right(temp_square))
        temp_square = self.get_board().right(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().right(temp_square)
            if temp_square is not None:
                moves_list.append(self.get_board().forward(temp_square))
                moves_list.append(self.get_board().back(temp_square))
        temp_square = self.get_board().left(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().left(temp_square)
            if temp_square is not None:
                moves_list.append(self.get_board().forward(temp_square))
                moves_list.append(self.get_board().back(temp_square))
        return moves_list






