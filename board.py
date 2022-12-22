from setup import *


class Board:
    colour = {0: LIGHT_GREEN,
              1: DARK_GREEN}

    board = pygame.Surface(dimensions)
    board.fill(DARK_GREEN)

    for i in range(LENGTH):
        for j in range(HEIGHT):
            pygame.draw.rect(board, colour[(i + j) % 2],
                             pygame.Rect(i * side_length, j * side_length, side_length, side_length), border_radius=2)

    def __init__(self):
        pass

    def draw(self, surf):
        surf.blit(self.board, (0, 0))
