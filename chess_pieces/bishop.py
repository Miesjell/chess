from chess_pieces.chess_piece import ChessPiece


class Bishop(ChessPiece):

    def __init__(self, color =""):
        super().__init__(color)
        self.piece = "bishop"
        self.directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    

    