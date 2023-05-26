from chessboard import *
import pygame
import sys

def redraw(screen, board, pieces, square_size, WHITE, GREY):
    # Draw the chess board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = GREY
            pygame.draw.rect(screen, color, [col * square_size, row * square_size, square_size, square_size])
            if board[row][col] != 0:
                # images are 55x55           
                piece_image = pieces[str(board[row][col])]
                piece_width, piece_height = piece_image.get_size()
                max_size = min(square_size - 25, piece_width, piece_height)
                # If bigger than square_size, resize it to 55x55
                piece_image = pygame.transform.smoothscale(piece_image, (max_size, max_size))
                # Make sure the chess pieces are centered on the squares
                center = (col * square_size + square_size // 2 - max_size // 2, row * square_size + square_size // 2 - max_size // 2)

                screen.blit(piece_image, center)

    # Update the display
    pygame.display.flip()

def main():

    chessboard = ChessBoard()
    
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)

    # Set up the display
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Chess")

    # Load the chess pieces
    pieces = {
        str(Pawn("white")): pygame.image.load("images/white_pawn.png"),
        str(Rook("white")): pygame.image.load("images/white_rook.png"),
        str(Knight("white")): pygame.image.load("images/white_knight.png"),
        str(Bishop("white")): pygame.image.load("images/white_bishop.png"),
        str(Queen("white")): pygame.image.load("images/white_queen.png"),
        str(King("white")): pygame.image.load("images/white_king.png"),
        str(Pawn("black")): pygame.image.load("images/black_pawn.png"),
        str(Rook("black")): pygame.image.load("images/black_rook.png"),
        str(Knight("black")): pygame.image.load("images/black_knight.png"),
        str(Bishop("black")): pygame.image.load("images/black_bishop.png"),
        str(Queen("black")): pygame.image.load("images/black_queen.png"),
        str(King("black")): pygame.image.load("images/black_king.png"),
    }

    # Define the chess board
    board = chessboard.current_position

    # Define the square size
    square_size = 80

    # Draw the chess board
    redraw(screen, board, pieces, square_size, WHITE, GREY)
           
    # Update the display
    pygame.display.flip()

    # Main game loop
    selected_piece = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if playr is in check and checkmate, game over
                
                # Get the clicked square
                x, y = pygame.mouse.get_pos()
                row = y // square_size
                col = x // square_size

                if selected_piece == 0:
                    # If no piece is selected, select the piece on the clicked square
                    selected_piece = board[row][col]

                    if selected_piece != 0 and selected_piece.color != chessboard.current_player:
                        selected_piece = 0

                    elif selected_piece != 0 and selected_piece.color == chessboard.current_player:
                        # Highlight the possible moves for the selected piece
                        moves, caps = selected_piece.possible_moves(chessboard, pre_check =True)
                        for move in (moves+caps):
                            # Highlight the possible moves for the selected piece and lower the saturation of the highlighted squares
                            pygame.draw.rect(screen, (255, 204, 229), [move[1] * square_size, move[0] * square_size, square_size, square_size])  

                            
                        pygame.display.flip()
                    else:   
                        # If no white piece is on the clicked square, do nothing
                        pass
                elif selected_piece != 0 and selected_piece.color == chessboard.current_player:
                    # If a piece is already selected, try to move the selected piece to the clicked square
                    # moves, caps = selected_piece.possible_moves(row, col, selected_piece, chessboard)
                    if (row, col) in moves or caps:
                        # Move the selected piece to the clicked square
                        selected_piece.move(row, col, chessboard)
                        # Switch players
                        
                        chessboard.current_player = "black" if chessboard.current_player == "white" else "white"
                        if chessboard.is_check():
                            print("Check!")
                            print(chessboard.is_checkmate())
                            if chessboard.is_check() and chessboard.is_checkmate():
                                print(f"GG, {chessboard.current_player} wins")
                                pygame.quit()
                                sys.exit()
                        selected_piece = 0
                        # Redraw the board
                        redraw(screen, board, pieces, square_size, WHITE, GREY)
                    else:
                        # If the clicked square is not a valid move for the selected piece, do nothing
                        selected_piece = 0
                        redraw(screen, board, pieces, square_size, WHITE, GREY)
                else:
                    selected_piece = 0
                    redraw(screen, board, pieces, square_size, WHITE, GREY)
                


if __name__ == '__main__':
    main()