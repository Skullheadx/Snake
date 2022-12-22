from setup import *


class Label:
    inset = 10

    def __init__(self, position, text, colour, background_colour, font_size):
        self.position = pygame.Vector2(position)
        self.raw_text = text
        self.colour = colour
        self.background_colour = background_colour
        self.font = pygame.font.SysFont("arial", font_size)
        self.text = self.font.render(self.raw_text, True, self.colour)
        self.length, self.height = self.text.get_size()

    def update(self, delta, raw_text=None, position=None):
        if raw_text is not None:
            self.raw_text = raw_text
            self.text = self.font.render(self.raw_text, True, self.colour)
            self.length, self.height = self.text.get_size()
        if position is not None:
            self.position = pygame.Vector2(position)

    def get_rect(self, centered=True):
        return pygame.Rect(self.position.x - self.inset - centered * self.length / 2,
                           self.position.y - self.inset - centered * self.height / 2,
                           self.length + 2 * self.inset, self.height + 2 * self.inset)

    def draw(self, surf, centered=True):
        if self.background_colour is not None:
            pygame.draw.rect(surf, self.background_colour, self.get_rect(centered), border_radius=5)
            pygame.draw.rect(surf, BLACK, self.get_rect(centered), width=3, border_radius=5)
        surf.blit(self.text, self.text.get_rect(center=self.get_rect(centered).center))
