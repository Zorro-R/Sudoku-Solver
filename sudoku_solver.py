board = [
    [5, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 5, 2, 9, 0, 1],
    [1, 6, 0, 0, 0, 0, 2, 5, 8],
    [9, 0, 0, 0, 0, 8, 4, 0, 3],
    [0, 0, 0, 9, 3, 7, 0, 0, 0],
    [6, 0, 8, 5, 0, 0, 0, 0, 9],
    [7, 2, 5, 0, 0, 0, 0, 9, 4],
    [8, 0, 3, 4, 7, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 5]
]


def display_board(board):
    '''
    Takes in a board object and displays it as a sudoku grid in the commandline.
    '''
    for i, row in enumerate(board):
        if i % 3 == 0:
            print()
            print()
        else:
            print()
        for j, value in enumerate(row):
            if j % 3 == 0:
                print("|", end="")
            print(value, end="|")
    print()

    return True


display_board(board)


def valid_entry(board, x, y, guess):
    '''
    Takes a board object, a position on the board: (x, y) from the top left corner,
    and an integer between 1-9 as a guess. Then checks the given row, column, and 
    3x3 square for the guessed number. If no conflict is found with pre-existing 
    entries returns True. Otherwise returns False.
    '''
    # Calculate 3x3 subgrid
    subgrid = [subrow[x - x % 3: x - x % 3 + 3]
               for subrow in board[y - y % 3: y - y % 3 + 3]]

    # Check row and column
    row = board[y]
    column = [row[x] for row in board]
    if guess in row or guess in column:
        return False

    # Check subgrid
    for row in subgrid:
        if guess in row:
            return False

    # If guess does not conflict with pre-existing entries return True
    return True


print(valid_entry(board, 3, 6, 1))
