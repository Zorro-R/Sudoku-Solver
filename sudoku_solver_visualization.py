import sys
import pygame
import copy
import time
from sudoku_solver import valid_entry, full_board, recursive_backtracking

# Constants
size = width, height = 800, 800
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
# Example sudoku puzzle from https://www.websudoku.com/?level=4&set_id=1044837704
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


def draw_board_outline(screen):
    '''
    Draws the outline of the sudoku board onto a pygame
    screen object

    Args:
    screen -> pygame.Surface
    Returns:
    None
    '''
    # Draw white background
    screen.fill(white)
    # Draw the board
    for i in range(10):
        # Indicate 3x3 areas on the board with thicker outlines
        if i % 3 == 0:
            line_width = 3
        else:
            line_width = 1

        # Draw vertical lines
        start_pos_vertical = 102 + i * 65, 102
        end_pos_vertical = 102 + i * 65, 686
        pygame.draw.line(
            screen, black, start_pos_vertical, end_pos_vertical, line_width)

        # Draw horizontal lines
        start_pos_horizontal = 102, 102 + i * 65
        end_pos_horizontal = 686, 102 + i * 65
        pygame.draw.line(
            screen, black, start_pos_horizontal, end_pos_horizontal, line_width)


def main():
    '''
    Visualizes the recursive backtracking algorithm on a sample puzzle
    using pygame.
    '''
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku Solver Visualization")

    font = pygame.font.SysFont("Times New Roman", 45)

    # A list that will track the progress of the algorithm
    list_of_boards = [copy.deepcopy(board)]
    # Run the backtracking algorithm
    recursive_backtracking(board, list_of_boards)

    isSolved = False
    isRunning = True

    # Game loop
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        if not isSolved:
            # Display each board configuration in order
            for i, board_configuration in enumerate(list_of_boards):
                # Draw the board outline
                draw_board_outline(screen)

                # Overlay the board values
                for y, row in enumerate(board_configuration):
                    for x, value in enumerate(row):
                        # If cell is not empty (i.e 0) display value
                        if value != 0:
                            textsurface = font.render(str(value), True, black)
                            screen.blit(
                                textsurface, (102 + 20 + x*65, 102 + 7 + y*65))

                # Update the screen
                pygame.display.update()

                # Add a delay
                # FIX: Causes the screen to freeze while algorithm is running
                pygame.time.delay(30)

            if i == len(list_of_boards) - 1:
                isSolved = True

    pygame.display.quit()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    main()
