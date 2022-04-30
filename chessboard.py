from Chess_Pieces.bishop import Bishop
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
            [0, 0, 0, Bishop("white"), 0, 0, 0, 0],
            [0, 0, Pawn("black"), Rook("black"), Knight("white"), 0, 0, 0],
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
        moves = []
        sel_piece = self.current_position[y][x]
        if sel_piece.piece == "pawn":
            moves = sel_piece.possible_moves(x, y, sel_piece, self)
        elif sel_piece.piece == "rook":
            moves = sel_piece.possible_moves(x, y, sel_piece, self)
        elif sel_piece.piece == "bishop":
            moves = sel_piece.possible_moves(x, y, sel_piece, self)
        elif sel_piece.piece == "knight":
            moves = sel_piece.possible_moves(x, y, sel_piece, self)
        elif sel_piece.piece == "queen":
            moves = sel_piece.possible_moves(x, y, sel_piece, self)
        elif sel_piece.piece == "king":
            moves = sel_piece.possible_moves(x, y, sel_piece, self)
        return moves


    def pos_queen_moves(self, x, y, sel_piece, board) -> list:
        """queen moves"""

    def pos_king_moves(self, x, y, sel_piece, board) -> list:
        """king moves"""

    def move(self, x, y):
        """
        If piece is chosen, show moves. if square of possible moves is click, play move
        keep track of whose turn it is"""
        self.pos_moves(x, y)


    def print_current(self):
        for x in self.current_position:
            print(x)
