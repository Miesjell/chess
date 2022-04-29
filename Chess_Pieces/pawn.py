from Chess_Pieces.chess_piece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, Color=""):
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

    def possible_moves(self, x: int, y: int, sel_piece, board) -> list:
        possible_moves = []
        if sel_piece.color == "white":
            if board.current_position[y + 1][x] == 0:
                possible_moves.append((x, y + 1))
                if not sel_piece.has_moved:
                    if board.current_position[y + 2][x] == 0:
                        possible_moves.append((x, y + 2))
        elif sel_piece.color == "black":
            if board.current_position[y - 1][x] == 0:
                possible_moves.append((x, y - 1))
                if not sel_piece.has_moved:
                    if board.current_position[y - 2][x] == 0:
                        possible_moves.append((x, y - 2))
        print(possible_moves)
        return possible_moves
