class ChessPiece:

    def __init__(self, color = ""):
        self.color = color
        self.piece = ""
        self.max_movement = ()
        # self.can_capture = can_capture

    def __str__(self):
        return f"{self.color} {self.piece}"

