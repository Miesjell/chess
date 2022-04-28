from Chess_Pieces.chess_piece import ChessPiece


class Rook(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "rook"
        self.has_moved = False