from label import Label
from setup import *


class Button(Label):

    def __init__(self, position, text, colour, background_colour, font_size, command):
        super().__init__(position, text, colour, background_colour, font_size)
        self.lightened_background = self.background_colour
        self.darkened_background = (
            max(background_colour[0] - 25, 0), max(background_colour[1] - 25, 0), max(background_colour[2] - 25, 0))
        self.command = command
        self.activated = False

    def update(self, delta, raw_text=None, position=None):
        super().update(delta, raw_text=raw_text, position=position)

        mx, my = pygame.mouse.get_pos()
        if self.get_rect().collidepoint(mx, my):
            self.background_colour = self.darkened_background

            if self.activated:
                return self.command

        else:
            self.background_colour = self.lightened_background
        return None

    def get_input(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.get_rect().collidepoint(pygame.mouse.get_pos()): # Left Mouse Button
                self.activated = True
