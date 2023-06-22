## Sudoku Board Solver:

# Algorithm Objectives:
# 1.) Pick Empty Square on Board
# 2.) Iterate nums 1-9 to Determine Possible Solution for Position
# 3.) Once a Solution was Found, Repeat Steps 1-3
# 4.) Backtrack if No Solution is Possible

#Algorithm Type Used: Backtrack Algorithm


def solve(board): # Solves the board Using empty_cell and is_valid Functions Defined Below
    empty_cell = find_empty(board)
    if not empty_cell:
        return True

    row, column = empty_cell

    for number in range(1, 10): # If given Number is Valid, Adds Number to Board Position
        if is_valid(board, number, (row, column)):
            board[row][column] = number

            if solve(board): # If False, This Resets Previous Position to 0 and Attempts Again
                return True

            board[row][column] = 0 

    return False


def is_valid(board, number, position): #Deterines if Given Value is Valid for Particular Position
    row, column = position

    # Check Row for Validity
    for i in range(len(board)):
        if i != column and board[row][i] == number:
            return False

    # Check Column for Validity
    for i in range(len(board)):
        if i != row and board[i][column] == number:
            return False

    # Check the Respective 3X3 Box for Validity
    box_start_row = 3 * (row // 3)
    box_start_column = 3 * (column // 3)

    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_column, box_start_column + 3):
            if (i, j) != position and board[i][j] == number:
                return False

    return True


def print_board(board): # Prints board in the Suduko Style Layout
    
    # Prints the Horizontal Lines
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- " * 12)

        # Prints the Vertical Lines
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" |", end="")

            print(f" {cell}", end="" if j != 8 else "\n")



def find_empty(board): # Finds Empty Spot on Board to Run Algorithm
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # i = row, j = column

    return None

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Call Functions to Solve and Show Before and After Boards
print("\n Starting Board: \n")
print_board(board)
solve(board)
print("\n_________________________\n")
print("\n Solved Board: \n")
print_board(board)
