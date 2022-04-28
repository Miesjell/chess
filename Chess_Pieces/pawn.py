from Chess_Pieces.chess_piece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "pawn"
        self.has_moved = False

    def first_move(self):
        """If a pawn has not moved, it can move forward either 1 or 2 spaces"""
        # if not self.has_moved:
        #     if self.color == "black":
        #         self.max_movement =
        #     elif self.color == "white":
        #         self.max_movement =