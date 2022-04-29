from Chess_Pieces.chess_piece import ChessPiece


class Rook(ChessPiece):

    def __init__(self, Color=""):
        super().__init__(Color)
        self.piece = "rook"
        self.has_moved = False

    def possible_moves(self, x, y, sel_piece, board) -> list:
        possible_moves = []
        possible_cap = []

        for hor in range(1, 8):
            if 0 <= (y + hor) <= 7:
                if board.current_position[y + hor][x] != 0:
                    for capture in board.check_capture(x, y + hor, sel_piece):
                        possible_cap.append(capture)
                    break
                elif 0 == board.current_position[y + hor][x]:
                    possible_moves.append((x, y + hor))

        for hor in range(-1, -8, -1):
            if 0 <= (y + hor) <= 7:
                if board.current_position[y + hor][x] != 0:
                    for capture in board.check_capture(x, y + hor, sel_piece):
                        possible_cap.append(capture)
                    break
                elif board.current_position[y + hor][x] == 0:
                    possible_moves.append((x, y + hor))

        for ver in range(1, 8):
            if 0 <= (x + ver) <= 7:
                if board.current_position[y][x + ver] != 0:
                    for capture in board.check_capture(x + ver, y, sel_piece):
                        possible_cap.append(capture)
                    break
                elif board.current_position[y][x + ver] == 0:
                    possible_moves.append((x + ver, y))
        print(f'moves: {possible_moves}, caps: {possible_cap}')
        return possible_moves, possible_cap