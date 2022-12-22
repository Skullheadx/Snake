from button import Button
from container import Container
from label import Label
from setup import *


class GameOver:
    def __init__(self, score, win=False):
        self.target = pygame.Vector2(center.x, dimensions.y * 1 / 3)
        self.position = pygame.Vector2(center.x, dimensions.y * 1.25)
        self.card = pygame.Surface((dimensions.x * 2 / 3, dimensions.y * 2 / 3))
        self.labels = [Label((center.x, dimensions.y / 3), "GAMEOVER", BLACK, None, 50),
                       Label(center, f"----( SCORE: {score} )----", BLACK, None, 30),
                       Button(center, "    PLAY AGAIN    ", BLACK, GRAY, 25, COMMAND_START),
                       Button(center, "          HELP          ", BLACK, GRAY, 25, COMMAND_HELP),
                       Button(center, "     MAIN MENU     ", BLACK, GRAY, 25, COMMAND_MENU)
                       ]
        if win:
            self.labels[0].update(0, raw_text="WIN")

        self.container = Container(self.position, self.labels, separation_distance=7)
        self.time = 0
        self.background_surface = None

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            self.container.get_input(event)
        self.position.y = max(self.target.y, self.position.y - pow(100, self.time / 1000))
        if self.position.y > center.y:
            self.time += delta
        return self.container.update(delta, position=self.position)

    def draw(self, surf):
        if self.background_surface is None:
            self.background_surface = pygame.Surface(dimensions)
            self.background_surface.blit(surf, (0, 0))
        surf.blit(self.background_surface, (0, 0))

        pygame.draw.rect(surf, YELLOW,
                         self.container.get_rect(),
                         border_radius=10)
        pygame.draw.rect(surf, BLACK,
                         self.container.get_rect(),
                         width=5, border_radius=10)
        self.container.draw(surf)
