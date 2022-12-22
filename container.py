from button import Button
from setup import *


class Container:
    inset = 20

    def __init__(self, position, buttons, separation_distance=10):
        self.position = pygame.Vector2(position)
        self.buttons = buttons
        self.separation_distance = separation_distance
        self.length, self.height = 0, 0
        self.spread()

    def spread(self):
        previous_position = self.position.y - self.buttons[0].get_rect().height / 2 + self.separation_distance / 2
        previous_height = 0
        self.length = 0
        self.height = self.buttons[0].get_rect().height / 2
        for button in self.buttons:
            button.position.y = previous_position + previous_height + self.separation_distance
            previous_position = button.position.y
            previous_height = button.get_rect().height
            self.height += button.get_rect().height + self.separation_distance
            self.length = max(self.length, button.get_rect().width)

    def update(self, delta, position=None):
        if position is not None:
            self.position = pygame.Vector2(position)
            self.spread()

        for button in self.buttons:
            status = button.update(delta)
            if status is not None:
                return status
        return

    def get_input(self, event):
        for button in self.buttons:
            if isinstance(button, Button):
                button.get_input(event)

    def get_rect(self):
        return pygame.Rect(self.position.x - self.inset - self.length / 2,
                           self.position.y - self.inset - self.buttons[0].get_rect().height,
                           self.length + 2 * self.inset, self.height + 2 * self.inset)

    def draw(self, surf):
        for button in self.buttons:
            button.draw(surf)
