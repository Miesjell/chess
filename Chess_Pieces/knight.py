from Chess_Pieces.chess_piece import ChessPiece


class Knight(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "knight"

    def possible_moves(self, x, y, sel_piece, board) -> list:
        """knight moves"""
        possible_moves = []
        possible_cap = []
        vectors = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
        for vec in vectors:
            if 0 <= (y + vec[1])<= 7 and 0 <= (x + vec[0]) <= 7:
                if board.current_position[y+vec[1]][x+vec[0]] == 0:
                    possible_moves.append((x+vec[0], y+vec[1]))
                if board.current_position[y + vec[1]][x + vec[0]] != 0:
                    for capture in self.check_capture(x + vec[0], y + vec[1], sel_piece, board):
                        possible_cap.append(capture)
        print(f'moves: {possible_moves}, caps: {possible_cap}')
        return possible_moves, possible_cap
