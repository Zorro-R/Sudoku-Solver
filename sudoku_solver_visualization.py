import sys
import pygame

# Constants
size = width, height = 800, 800
white = 255, 255, 255
black = 0, 0, 0


def main():
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku Solver Visualization")

    font = pygame.font.SysFont("Times New Roman", 30)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

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

        # Overlay the board values
        textsurface = font.render("Test", True, black)

        # Update the screen
        screen.blit(textsurface, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    main()
