from chess_pieces.chess_piece import ChessPiece


class King(ChessPiece):

    def __init__(self, color =""):
        super().__init__(color)
        self.piece = "king"
        self.has_moved = False
        self.directions = [(1, 0), (1, 1), (0, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        self.max_iter = 1
    

    def check_castling(self, board, dx):
        """Checks if castling is possible in the given direction"""
        # check if postions between king and rook are empty
        to_rook = 3 if dx > 0 else 4
        for i in range(1, to_rook):
            if board.current_position[self.x + dx * i][self.y] != 0:
                return False
 
        # check if rook is in the corner and has not moved
        if board.current_position[self.x + dx * to_rook][self.y] != 0 and \
            board.current_position[self.x + dx * to_rook][self.y].piece == "rook" and \
            not board.current_position[self.x + dx * to_rook][self.y].has_moved:
            return True

        return False


    def possible_moves(self, board, pre_check = False) -> list:
        moves, caps = super().possible_moves(board, pre_check=pre_check)

        if not self.has_moved:
            # Castling kingside
            if self.check_castling(board, dx = 1):
                moves.append((self.x + 2, self.y))

            # Castling queenside
            if self.check_castling(board, dx = -1):
                moves.append((self.x - 2, self.y))

        return moves, caps
