from Chess_Pieces.bishop import Bishop
from Chess_Pieces.chess_piece import ChessPiece
from Chess_Pieces.king import King
from Chess_Pieces.knight import Knight
from Chess_Pieces.pawn import Pawn
from Chess_Pieces.queen import Queen
from Chess_Pieces.rook import Rook


class ChessBoard:

    def __init__(self):
        self.in_check = False
        self.start_position = [
            [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"),
             Knight("white"), Rook("white")],
            [0, Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"),
             Pawn("white")],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"),
             Pawn("black")],
            [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"),
             Knight("black"), Rook("black")]]
        self.current_position = self.start_position

    def is_check(self):
        """method to check for check for check when any move is made. Check for both sides. If player making move
         is in check, don't allow"""
        self.is_checkmate()

    def is_checkmate(self):
        print("if is_check == True, then run this function")

    def reset_board(self):
        print("Supposed to reset the board to start_position")

    def pos_moves(self, x, y):
        sel_piece = self.current_position[y][x]
        if sel_piece.piece == "pawn":
            moves = self.pos_pawn_moves(x, y, sel_piece)
        elif sel_piece.piece == "rook":
            moves = self.pos_rook_moves(x, y, sel_piece)
        elif sel_piece.piece == "bishop":
            moves = self.pos_bishop_moves(x, y, sel_piece)
        elif sel_piece.piece == "knight":
            moves = self.pos_bishop_moves(x, y, sel_piece)
        elif sel_piece.piece == "queen":
            moves = self.pos_bishop_moves(x, y, sel_piece)
        elif sel_piece.piece == "king":
            moves = self.pos_bishop_moves(x, y, sel_piece)
        return moves

    def pos_pawn_moves(self, x: int, y: int, sel_piece) -> list:
        possible_moves = []
        if sel_piece.color == "white":
            if self.current_position[y + 1][x] == 0:
                possible_moves.append((x, y + 1))
                if not sel_piece.has_moved:
                    if self.current_position[y + 2][x] == 0:
                        possible_moves.append((x, y + 2))
        elif sel_piece.color == "black":
            if self.current_position[y - 1][x] == 0:
                possible_moves.append((x, y - 1))
                if not sel_piece.has_moved:
                    if self.current_position[y - 1][x] == 0:
                        possible_moves.append((x, y - 2))
        print(possible_moves)
        return possible_moves

    def pos_rook_moves(self, x, y, sel_piece) -> list:
        possible_moves = []
        possible_cap = []

        for hor in range(1, 8):
            if 0 <= (y + hor) <= 7:
                if self.current_position[y + hor][x] != 0:
                    for capture in self.check_capture(x, y + hor, sel_piece):
                        possible_cap.append(capture)
                    break
                elif 0 == self.current_position[y + hor][x]:
                    possible_moves.append((x, y + hor))

        for hor in range(-1, -8, -1):
            if 0 <= (y + hor) <= 7:
                if self.current_position[y + hor][x] != 0:
                    for capture in self.check_capture(x, y + hor, sel_piece):
                        possible_cap.append(capture)
                    break
                elif self.current_position[y + hor][x] == 0:
                    possible_moves.append((x, y + hor))

        for ver in range(1, 8):
            if 0 <= (x + ver) <= 7:
                if self.current_position[y][x + ver] != 0:
                    for capture in self.check_capture(x + ver, y, sel_piece):
                        possible_cap.append(capture)
                    break
                elif self.current_position[y][x + ver] == 0:
                    possible_moves.append((x + ver, y))

        for ver in range(-1, -8, -1):
            if 0 <= (x + ver) <= 7:
                if self.current_position[y][x + ver] != 0:
                    for capture in self.check_capture(x + ver, y, sel_piece):
                        possible_cap.append(capture)
                    break
                elif self.current_position[y][x + ver] == 0:
                    possible_moves.append((x + ver, y))
        print(f'moves: {possible_moves}, caps: {possible_cap}')
        return possible_moves, possible_cap

    def pos_bishop_moves(self, x, y, sel_piece) -> list:
        """Bishop moves"""
        possible_moves = []
        for hor in range(1, 8):
            if self.current_position[y + hor][x + hor] != 0:
                break
            elif self.current_position[y + hor][x + hor] == 0:
                possible_moves.append((x + hor, y + hor))

        for hor in range(-1, -8, -1):
            if self.current_position[y + hor][x + hor] != 0:
                break
            elif self.current_position[y + hor][x + hor] == 0:
                possible_moves.append((x + hor, y + hor))

        for ver in range(1, 8):
            if self.current_position[y + ver][x + ver] != 0:
                break
            elif self.current_position[y + ver][x + ver] == 0:
                possible_moves.append((x + ver, y + ver))

        for ver in range(-1, -8, -1):
            if self.current_position[y + ver][x + ver] != 0:
                break
            elif self.current_position[y + ver][x + ver] == 0:
                possible_moves.append((x + ver, y + ver))
        print(possible_moves)
        return possible_moves

    def pos_knight_moves(self, x, y, sel_piece) -> list:
        """knight moves"""

    def pos_queen_moves(self, x, y, sel_piece) -> list:
        """queen moves"""

    def pos_king_moves(self, x, y, sel_piece) -> list:
        """king moves"""

    def move(self, x, y):
        """
        If piece is chosen, show moves. if square of possible moves is click, play move
        keep track of whose turn it is"""
        self.pos_moves(x, y)

    def check_capture(self, x: int, y: int, sel_piece: object) -> list:
        """Checks if capture possible. Maybe under class """
        possible_captures = []

        if sel_piece.color != self.current_position[y][x].color:
            possible_captures.append((x, y))
        return possible_captures

    def print_current(self):
        for x in self.current_position:
            print(x)
