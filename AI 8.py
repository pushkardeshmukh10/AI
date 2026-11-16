
# Tic-Tac-Toe using Minimax Algorithm

# Create an empty board with 9 positions
board = [" "] * 9


# Function to display the game board
def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} ")
    print("-----------")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("-----------")
    print(f" {b[6]} | {b[7]} | {b[8]} \n")


# Function to check whether a player has won
def check_win(b, p):

    # All possible winning combinations
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    # Return True if any winning combination matches
    return any(b[i] == b[j] == b[k] == p for i, j, k in wins)


# Minimax algorithm to find the best possible score
def minimax(b, is_max):

    # If AI (O) wins, return +1
    if check_win(b, "O"):
        return 1

    # If human (X) wins, return -1
    if check_win(b, "X"):
        return -1

    # If no empty position remains, it is a draw
    if " " not in b:
        return 0

    # AI tries to maximize the score
    if is_max:
        best = -99

        # Check every empty position
        for i in range(9):
            if b[i] == " ":

                # Make AI move
                b[i] = "O"

                # Recursively calculate score
                best = max(best, minimax(b, False))

                # Undo the move
                b[i] = " "

        return best

    # Human tries to minimize the score
    else:
        best = 99

        # Check every empty position
        for i in range(9):
            if b[i] == " ":

                # Make human move
                b[i] = "X"

                # Recursively calculate score
                best = min(best, minimax(b, True))

                # Undo the move
                b[i] = " "

        return best


# Function to select the best move for AI
def ai_best_move(b):

    val, move = -99, -1

    # Check all empty positions
    for i in range(9):
        if b[i] == " ":

            # Try placing AI symbol
            b[i] = "O"

            # Calculate the move score
            score = minimax(b, False)

            # Undo the move
            b[i] = " "

            # Select the move with the highest score
            if score > val:
                val, move = score, i

    return move


# Main function to play the game
def play_game():

    print("========================================")
    print("       O vs X GAME (TIC-TAC-TOE)")
    print("========================================")
    print("You are X. The AI is O.")

    # Display position numbers
    print("Positions are numbered 0 to 8:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 \n")

    # Repeat until someone wins or game draws
    while True:

        print_board(board)

        # Take input from human player
        try:
            move = int(input("Enter your move (0-8): "))

            # Check whether move is valid
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Choose an empty spot between 0 and 8.")
                continue

        except ValueError:
            print("Please enter a valid integer number!")
            continue

        # Place human symbol X
        board[move] = "X"

        # Check whether human wins
        if check_win(board, "X"):
            print_board(board)
            print("Congratulations, you win!")
            break

        # Check whether game is a draw
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break

        # AI calculates its best move
        print("AI (O) is thinking...")
        ai_move = ai_best_move(board)

        # Place AI symbol O
        board[ai_move] = "O"

        # Check whether AI wins
        if check_win(board, "O"):
            print_board(board)
            print("AI (O) wins! Better luck next time.")
            break

        # Check whether game is a draw
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break


# Program execution starts here
if __name__ == "__main__":
    play_game()
