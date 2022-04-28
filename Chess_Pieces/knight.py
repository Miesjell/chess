from Chess_Pieces.chess_piece import ChessPiece


class Knight(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "knight"