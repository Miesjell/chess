from chess_pieces.bishop import Bishop
from chess_pieces.king import King
from chess_pieces.knight import Knight
from chess_pieces.pawn import Pawn
from chess_pieces.queen import Queen
from chess_pieces.rook import Rook

class ChessBoard:

    def __init__(self):
        self.current_player = "white"
        self.start_position = [
            [Rook("white")  , Pawn("white"), 0, 0, 0, 0, Pawn("black"), Rook("black")  ],
            [Knight("white"), Pawn("white"), 0, 0, 0, 0, Pawn("black"), Knight("black")],
            [Bishop('white'), Pawn("white"), 0, 0, 0, 0, Pawn("black"), Bishop("black")],
            [Queen("white") , Pawn("white"), 0, 0, 0, 0, Pawn("black"), Queen("black") ],
            [King("white")  , Pawn("white"), 0, 0, 0, 0, Pawn("black"), King("black")  ],
            [Bishop("white"), Pawn("white"), 0, 0, 0, 0, Pawn("black"), Bishop("black")],
            [Knight("white"), Pawn("white"), 0, 0, 0, 0, Pawn("black"), Knight("black")],
            [Rook("white")  , Pawn("white"), 0, 0, 0, 0, Pawn("black"), Rook("black")  ],
            ]
        self.current_position = self.start_position
        self.current_king = {"white": (4, 0), 
                             "black": (4, 7)}

        for i in range(8):
            for j in range(8):
                piece = self.start_position[i][j]
                if piece != 0:
                    piece.x = i
                    piece.y = j          

    def __str__(self):
        board = ""
        for row in self.current_position:
            for piece in row:
                if piece == 0:
                    board += "0 "
                else:
                    board += str(piece) + " "
            board += "\n"
        return board
    
    def is_check(self):
        # Check if the king is in check
        king_pos = self.current_king[self.current_player]
        for i in range(8):
            for j in range(8):
                piece = self.current_position[i][j]
                if piece != 0 and piece.color != self.current_player:
                    _, caps = piece.possible_moves(self, pre_check = False)
                    if (king_pos[0], king_pos[1]) in caps:
                        return True
        return False

    def is_checkmate(self):
        """if is_check is true and no valid moves are available, then checkmate"""
        for i in range(8):
            for j in range(8):
                piece = self.current_position[i][j]
                if piece != 0 and piece.color == self.current_player:
                    print(i,j)
                    print(self.current_player)
                    moves, caps = piece.possible_moves(self, pre_check = True)
                    if len(moves) > 0 or len(caps) > 0:
                        print(moves)
                        return False         
        return True

    def reset_board(self):
        """"Resets the board to its starting position"""
        self.current_position = self.start_position

    def print_current(self):
        for obj in self.current_position:
            print(obj)
