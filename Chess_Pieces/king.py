from Chess_Pieces.chess_piece import ChessPiece


class King(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "king"
        self.has_moved = False
