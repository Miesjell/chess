from chess_pieces.chess_piece import ChessPiece


class Queen(ChessPiece):

    def __init__(self, color = ""):
        super().__init__(color)
        self.piece = "queen"
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    