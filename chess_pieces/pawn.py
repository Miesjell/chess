from chess_pieces.chess_piece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, color=""):
        super().__init__(color)
        self.piece = "pawn"
        self.has_moved = False
        self.directions = [(1, 1), (-1, 1)] 

    def possible_capture(self, board, pre_check = False) -> list:
        possible_cap = []
        dir = 1 if self.color == "white" else -1

        if 0 <= self.x + dir <= 7 and 0 <= self.y + dir <= 7 and board.current_position[self.x + dir][self.y + dir] != 0 \
            and board.current_position[self.x + dir][self.y + dir].color != self.color:
            if pre_check:
                if self.is_valid_move(self.x + dir, self.y + dir, board):
                    possible_cap.append((self.x + dir, self.y + dir))
            else:
                possible_cap.append((self.x + dir, self.y + dir))

        if 0 <= self.x - dir <= 7 and 0 <= self.y + dir <= 7 and board.current_position[self.x - dir][self.y + dir] != 0 \
            and board.current_position[self.x - dir][self.y + dir].color != self.color:
            if pre_check:
                if self.is_valid_move(self.x - dir, self.y + dir, board):
                    possible_cap.append((self.x - dir, self.y + dir))
            else:
                possible_cap.append((self.x - dir, self.y + dir))

        return possible_cap


    def possible_moves(self, board, pre_check = False) -> list:
        possible_moves = []
        dir = 1 if self.color == "white" else -1

        
        if self.y + dir >= 0 and self.y + dir <= 7 and board.current_position[self.x][self.y + dir] == 0:
            if pre_check:
                if self.is_valid_move(self.x, self.y + dir, board):
                    print("here")
                    possible_moves.append((self.x, self.y + dir))
            else:
                possible_moves.append((self.x, self.y + dir))
            
            if not self.has_moved:
                if self.y + dir * 2 <= 7 and board.current_position[self.x][self.y + dir * 2] == 0:
                    if pre_check:
                        if self.is_valid_move(self.x, self.y + dir * 2, board):
                            print("here")
                            possible_moves.append((self.x, self.y + dir * 2))
                    else:
                        possible_moves.append((self.x, self.y + dir * 2))

        possible_cap = self.possible_capture(board, pre_check=pre_check)
        return possible_moves, possible_cap


