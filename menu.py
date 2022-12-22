from button import Button
from container import Container
from label import Label
from setup import *


class Menu:
    inset = 0.1

    def __init__(self):
        self.labels = [Label((center.x, dimensions.y / 3), "SNAKE", BLACK, BLUE, 100),
                       Button(center, "        PLAY        ", DARK_GRAY, GRAY, 30, COMMAND_START),
                       Button(center, "        HELP        ", DARK_GRAY, GRAY, 30, COMMAND_HELP),
                       Button(center, "        QUIT        ", DARK_GRAY, GRAY, 30, COMMAND_EXIT)
                       ]
        self.container = Container((center.x, dimensions.y * 2 / 5), self.labels)

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            self.container.get_input(event)

        return self.container.update(delta)

    def draw(self, surf):
        surf.fill(DARK_GREEN)
        pygame.draw.rect(surf, LIGHT_GREEN,
                         pygame.Rect(self.inset * dimensions.x,
                                     self.inset * dimensions.y,
                                     dimensions.x * (1 - 2 * self.inset),
                                     dimensions.y * (1 - 2 * self.inset)),
                         border_radius=15)
        pygame.draw.rect(surf, LIGHT_GREEN,
                         pygame.Rect(self.inset * dimensions.x,
                                     self.inset * dimensions.y,
                                     dimensions.x * (1 - 2 * self.inset),
                                     dimensions.y * (1 - 2 * self.inset)),
                         width=20, border_radius=15)
        self.container.draw(surf)
