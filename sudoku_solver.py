import copy

# Idea sparked by this post https://hackernoon.com/sudoku-and-backtracking-6613d33229af
# Further inspiration from https://www.reddit.com/r/Python/comments/empp5x/oc_updated_version_of_my_recent_maze_finding/


def display_board(board):
    '''
    Takes in a board object and displays it as a sudoku grid in the commandline.

    Args:
    board -> List[List[]]
    Returns:
    True
    '''
    for y, row in enumerate(board):
        if y % 3 == 0:
            print("\n---------------------")

        else:
            print()
        for x, value in enumerate(row):
            if x % 3 == 0:
                print("|", end="")
            print(value, end="|")
    print()
    print()

    return True


def valid_entry(board, x, y, guess):
    '''
    Takes a board object, a position on the board: (x, y) from the top left corner,
    and an integer between 1-9 as a guess. Then checks the given row, column, and 
    3x3 square for the guessed number. If no conflict is found with pre-existing 
    entries returns True. Otherwise returns False.

    Args: 
    board -> List[List[]]
    x, y, guess -> Int
    Returns:
    True if entry does not conflict with pre-existing entries 
    else False
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


def full_board(board):
    '''
    Checks if all squares on the board have been filled. 
    Returns True if this is the case.

    Args:
    board -> List[List[]]
    Returns:
    True if no cell is 0 (i.e empty)
    else False
    '''
    for row in board:
        for value in row:
            if value == 0:
                return False

    return True


def recursive_backtracking(board, list_of_boards=[], save_boards=True):
    '''
    Function that applies recursive backtracking to a board object.
    Returns True if the board could be solved and False if no solution 
    could be found. Modifies the board object itself. Also appends each
    board configuration to a list_of_boards (Can be disabled by setting
    save_boards to False).

    Args:
    board -> List[List[]]
    list_of_boards -> List[]
    save_boards -> Bool
    Returns:
    True if board can be filled given constraints
    else False
    '''
    # Base case - board is full
    if full_board(board):
        return True

    # Recursive case - board isn't full
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            if value == 0:  # If cell is empty
                for guess in range(1, 10):
                    # If guess does not cause a conflict, save the guess to the board
                    if valid_entry(board, x, y, guess):
                        board[y][x] = guess

                        # If save_boards is True append copy of board to list_of_boards
                        if save_boards:
                            list_of_boards.append(copy.deepcopy(board))
                        # If this candidate guess works return True
                        if recursive_backtracking(board, list_of_boards, save_boards):
                            return True
                        # Otherwise reset the cell and try the next guess
                        else:
                            board[y][x] = 0

                # In the case that no guess works, the board cannot be solved so we return False
                return False


# Sudoku puzzle taken from https://www.websudoku.com/?level=1&set_id=1559770422
board1 = [
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

# Another sudoku puzzle taken from https://www.websudoku.com/?level=4&set_id=1044837704
board2 = [
    [0, 6, 0, 0, 0, 0, 0, 5, 4],
    [0, 5, 7, 0, 0, 3, 9, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 5],
    [0, 0, 3, 1, 0, 4, 2, 0, 0],
    [7, 0, 8, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 6, 4, 0, 0, 5, 2, 0],
    [2, 4, 0, 0, 0, 0, 0, 1, 0]
]


def main():
    '''
    Runs the recursive backtracking algorithm on two example puzzles.
    '''
    # Run backtracking algorithm on board 1
    print("Example 1")
    display_board(board1)
    list_of_boards1 = [copy.deepcopy(board1)]
    recursive_backtracking(board1, list_of_boards1)
    print("Example 1 Solution")
    display_board(board1)

    # Run backtracking algorithm on board 2
    print("Example 2")
    display_board(board2)
    list_of_boards2 = [copy.deepcopy(board2)]
    recursive_backtracking(board2, list_of_boards2)
    print("Example 2 Solution")
    display_board(board2)


if __name__ == "__main__":
    main()
