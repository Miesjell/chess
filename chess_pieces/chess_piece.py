import copy


class ChessPiece:

    def __init__(self, color = ""):
        self.color = color
        self.piece = ""
        self.max_movement = ()
        self.x = 0
        self.y = 0
    

    def __str__(self):
        return f"{self.color}_{self.piece}"

    def check_capture(self, x: int, y: int, board : object) -> list:
        """Checks if capture possible. Maybe under class """

        if self.color != board.current_position[x][y].color:
            return True
        else:
            return False

    def possible_moves(self, board : object, pre_check = False) -> list:
        """Returns possible moves and captures"""

        if hasattr(self, "max_iter"):
            max_iter = self.max_iter + 1
        else:
            max_iter = 8
        directions = self.directions

        possible_moves = []
        possible_cap = []
        

        for direction in directions:
            for i in range(1, max_iter):
                if i > 1 and 2 in direction:
                    continue
                new_x = self.x + direction[0] * i
                new_y = self.y + direction[1] * i

                if 0 <= new_x <= 7 and 0 <= new_y <= 7:

                    if board.current_position[new_x][new_y] != 0:
                        if self.check_capture(new_x, new_y, board):
                            if pre_check:
                                if self.is_valid_move(new_x, new_y, board):
                                    possible_cap.append((new_x, new_y))
                            else:
                                possible_cap.append((new_x, new_y))   
                        break
                    elif board.current_position[new_x][new_y] == 0:
                        if pre_check and self.is_valid_move(new_x, new_y, board):
                            possible_moves.append((new_x, new_y))

        return possible_moves, possible_cap  
                        

    def move(self, to_x = int, to_y = int, board = object):
        """Moves piece to x, y"""

        moves, caps = self.possible_moves(board, pre_check = True)


        if (to_x, to_y) in moves or caps:
             # move piece to new position
            board.current_position[to_x][to_y] = board.current_position[self.x][self.y]
            board.current_position[self.x][self.y] = 0
            
            if board.current_position[to_x][to_y].piece in ["king", "rook", "pawn"]:
                board.current_position[to_x][to_y].has_moved = True

                # castling
                if self.piece == "king":
                    board.current_king[self.color] = (to_x, to_y)
                    if to_x == self.x + 2:
                        board.current_position[to_x - 1][to_y] = board.current_position[7][to_y]
                        board.current_position[7][to_y] = 0
                        board.current_position[to_x - 1][to_y].has_moved = True
                        board.current_position[to_x - 1][to_y].x = to_x - 1
                        board.current_position[to_x - 1][to_y].y = to_y
                    elif to_x == self.x - 2:
                        board.current_position[to_x + 1][to_y] = board.current_position[0][to_y]
                        board.current_position[0][to_y] = 0
                        board.current_position[to_x + 1][to_y].has_moved = True
                        board.current_position[to_x + 1][to_y].x = to_x + 1
                        board.current_position[to_x + 1][to_y].y = to_y

            
            self.x = to_x
            self.y = to_y
            
            

        else:
            print("Invalid move. Try again.")
            return False
        
    def is_valid_move(self, to_x, to_y, board):
        """
        Check if a move is valid by checking that it doesn't put the player's own king in check.
        """
        # Simulate the move
        old_x, old_y = self.x, self.y
        old_piece = board.current_position[to_x][to_y]
        board.current_position[to_x][to_y] = self
        board.current_position[old_x][old_y] = 0
        self.x, self.y = to_x, to_y

        if self.piece == "king":
            board.current_king[self.color] = (to_x, to_y)

        king_pos = board.current_king[self.color]
        for i in range(8):
            for j in range(8):
                other_piece = board.current_position[i][j]
                if other_piece != 0 and other_piece.color != self.color:
                    _, caps = other_piece.possible_moves(board, pre_check = False)
                    if (king_pos[0], king_pos[1]) in caps:
                        # Move puts the king in check, so it's not valid
                        # Undo the move and return False
                        board.current_position[to_x][to_y] = 0
                        board.current_position[old_x][old_y] = self
                        self.x, self.y = old_x, old_y
                        return False

        if self.piece == "king":
            board.current_king[self.color] = (old_x, old_y)
        # Undo the move and return True
        board.current_position[to_x][to_y] = old_piece
        board.current_position[old_x][old_y] = self
        self.x, self.y = old_x, old_y
        return True
