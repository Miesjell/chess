from Chess_Pieces.chess_piece import ChessPiece


class Queen(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "queen"