#ProficiencyTest: Tic-Tac-Toe game, Elisheva Kibbie

import random

# This prints the tik-tak-toe board game. 
def print_board(board):
    print("\nBoard:")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# This Function checks for a winner🤴🙀
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Checks rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Checks columns
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Diagonals
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # backwards diagonals
        return True
    
    return False

# Function to check if the board is full with no-winners
def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# This tells the computer to take its turn
def computer_turn(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

# Main game loop
def play_game():
    # This Creates the empty board(oﾟvﾟ)ノ
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    print("To make a move, enter the row and column (both between 1 and 3).")
    print("For example, '1 1' will place your mark in the top-left corner.")

    while True:
        # This defines the users turn
        print_board(board)
        while True:
            try:
                user_input = input("Your turn! Enter row and column (1-3) separated by space: ")
                row, col = map(int, user_input.split())
                if board[row-1][col-1] == " ":
                    board[row-1][col-1] = "X"
                    break
                else:
                    print("That spot is already taken. sorry not sorry.")
            except (ValueError, IndexError):
                print("thats not between 1-3. Please enter row and column between 1 and 3.")

        # This Checks if user wins
        if check_winner(board, "X"):
            print_board(board)
            print("Congrats! You win!")
            break
        
        if board_full(board):
            print_board(board)
            print("It's a Tie!")
            break

        # Computers turn
        print("Computer's turn (O)...")
        row, col = computer_turn(board)
        board[row][col] = "O"

        # Checks if computer wins
        if check_winner(board, "O"):
            print_board(board)
            print("Sorry, the computer wins!")
            break
        
        if board_full(board):
            print_board(board)
            print("It's a Tie!")
            break

# This function at the bottom starts the game. 
play_game()
