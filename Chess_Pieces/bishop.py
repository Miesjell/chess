from Chess_Pieces.chess_piece import ChessPiece


class Bishop(ChessPiece):

    def __init__(self, Color =""):
        super().__init__(Color)
        self.piece = "bishop"

    def possible_moves(self, x, y, sel_piece, chess_board) -> list:
        """Bishop moves"""
        possible_moves = []
        possible_cap = []

        for diag in range(1, 8):
            if 0 <= (x + diag) <= 7 and 0 <= (y + diag) <= 7:
                if chess_board.current_position[y + diag][x + diag] != 0:
                    for capture in chess_board.check_capture(x + diag, y + diag, sel_piece):
                        possible_cap.append(capture)
                    break
                elif chess_board.current_position[y + diag][x + diag] == 0:
                    possible_moves.append((x + diag, y + diag))

        for diag in range(-1, -8, -1):
            if 0 <= (x + diag) <= 7 and 0 <= (y + diag) <= 7:
                if chess_board.current_position[y + diag][x + diag] != 0:
                    for capture in chess_board.check_capture(x + diag, y + diag, sel_piece):
                        possible_cap.append(capture)
                    break
                elif chess_board.current_position[y + diag][x + diag] == 0:
                    possible_moves.append((x + diag, y + diag))

        for diag in range(1, 8):
            if 0 <= (x - diag) <= 7 and 0 <= (y + diag) <= 7:
                if chess_board.current_position[y + diag][x - diag] != 0:
                    for capture in chess_board.check_capture(x - diag, y + diag, sel_piece):
                        possible_cap.append(capture)
                    break
                elif chess_board.current_position[y + diag][x - diag] == 0:
                    possible_moves.append((x - diag, y + diag))
        print(f'moves: {possible_moves}, caps: {possible_cap}')
        return possible_moves, possible_cap