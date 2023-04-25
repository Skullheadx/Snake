import pygame

pygame.init()

LENGTH, HEIGHT = 20, 20
side_length = 640 / LENGTH
x_unit = pygame.Vector2(side_length, 0)
y_unit = pygame.Vector2(0, side_length)
dimensions = pygame.Vector2(side_length * LENGTH, side_length * HEIGHT)
center = pygame.Vector2(dimensions.x / 2, dimensions.y / 2)

pygame.display.set_caption("Snake Game")
pygame.display.set_icon(pygame.image.load("assets/logo.png"))

COMMAND_START = 0
COMMAND_EXIT = 1
COMMAND_LOSE = 2
COMMAND_WIN = 3
COMMAND_HELP = 4
COMMAND_MENU = 5

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (58, 58, 58)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (29, 170, 52)
DARK_GREEN = (25, 147, 45)
BLUE = (18, 82, 170)
LIGHT_BLUE = (10, 37, 211)
DARK_BLUE = (8, 25, 137)
YELLOW = (221, 219, 84)


def mod(pos):
    return pygame.Vector2(pos.x % dimensions.x, pos.y % dimensions.y)


sounds = {
    "eat": pygame.mixer.Sound("assets/sounds/eating-sound-effect.wav")
}

sounds["eat"].set_volume(0.1)

pygame.mixer.music.load("assets/sounds/chill-abstract-intention.wav")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)
