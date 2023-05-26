from chess_pieces.chess_piece import ChessPiece


class Knight(ChessPiece):

    def __init__(self, color =""):
        super().__init__(color)
        self.piece = "knight"
        self.directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        self.max_iter = 1

