class ChessPiece:

    def __init__(self, color = ""):
        self.color = color
        self.piece = ""
        self.max_movement = ()


    def __str__(self):
        return f"{self.color} {self.piece}"

    def check_capture(self, x: int, y: int, sel_piece: object, board : object) -> list:
        """Checks if capture possible. Maybe under class """
        possible_captures = []

        if sel_piece.color != board.current_position[y][x].color:
            possible_captures.append((x, y))
        return possible_captures

