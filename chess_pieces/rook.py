from chess_pieces.chess_piece import ChessPiece


class Rook(ChessPiece):

    def __init__(self, color=""):
        super().__init__(color)
        self.piece = "rook"
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.has_moved = False

    