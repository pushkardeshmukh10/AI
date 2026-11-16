# Function to check whether a number can be placed safely
def is_safe(board, row, col, num):

    # Check the entire row
    for i in range(9):
        if board[row][i] == num:
            return False
    # If number already exists in row, return False.

    # Check the entire column
    for i in range(9):
        if board[i][col] == num:
            return False
    # If number already exists in column, return False.

    # Find starting position of 3x3 box
    r = row - row % 3
    c = col - col % 3
    # r = Starting row of 3x3 box.
    # c = Starting column of 3x3 box.

    # Check the 3x3 box
    for i in range(3):
        for j in range(3):
            if board[r + i][c + j] == num:
                return False
    # If number already exists in 3x3 box, return False.

    return True
    # Number is safe to place.


# Function to solve Sudoku
def solve(board):

    # Traverse all rows/coulumns
    for row in range(9):
        for col in range(9):

            # Check whether the cell is empty
            if board[row][col] == 0:

                # Try numbers from 1 to 9
                for num in range(1, 10):

                    # Check whether number is safe
                    if is_safe(board, row, col, num):

                        # Place number in empty cell
                        board[row][col] = num

                        # Recursively solve remaining puzzle
                        if solve(board):
                            return True

                        # Backtracking: Remove incorrect number
                        board[row][col] = 0

                # No valid number found
                return False

    # All cells are filled successfully
    return True


# Initial Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Check and display solution
if solve(board):

    print("Solved Sudoku:")

    # Print each row
    for row in board:
        print(row)

else:
    print("No solution")
