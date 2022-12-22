from button import Button
from container import Container
from label import Label
from setup import *


class Help:
    inset = 0.1

    def __init__(self):
        self.labels = [Label((center.x, dimensions.y / 3), "HELP", BLACK, BLUE, 70),
                       Label(center, "WASD or ARROW Keys to move.", DARK_GRAY, None, 25),
                       Label(center, "Don't run into yourself.", DARK_GRAY, None, 25),
                       Label(center, "Eat apples to grow larger.", DARK_GRAY, None, 25),
                       Label(center, "Survive as long as possible.", DARK_GRAY, None, 25),
                       Button(center, "Return to Main Menu", DARK_GRAY, GRAY, 25, COMMAND_MENU)
                       ]
        self.container = Container((center.x, dimensions.y * 2 / 5), self.labels, separation_distance=7)

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            self.container.get_input(event)

        return self.container.update(delta)

    def draw(self, surf):
        surf.fill(DARK_GREEN)
        pygame.draw.rect(surf, LIGHT_GREEN, pygame.Rect(self.inset * dimensions.x, self.inset * dimensions.y,
                                                        dimensions.x * (1 - 2 * self.inset),
                                                        dimensions.y * (1 - 2 * self.inset)), border_radius=15)
        pygame.draw.rect(surf, LIGHT_GREEN, pygame.Rect(self.inset * dimensions.x, self.inset * dimensions.y,
                                                        dimensions.x * (1 - 2 * self.inset),
                                                        dimensions.y * (1 - 2 * self.inset)), width=20,
                         border_radius=15)
        self.container.draw(surf)
