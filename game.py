from board import Board
from food_manager import FoodManager
from label import Label
from player import Player
from setup import *


class Game:

    def __init__(self):
        self.board = Board()
        self.food_manager = FoodManager()
        self.snake = Player(center - 2 * x_unit)
        self.fast_forward = False
        self.ff_label = Label((0, 0), ">>", WHITE, None, 50)

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            elif event.type == pygame.KEYDOWN:
                self.snake.get_input(event)
                if event.key == pygame.K_SPACE:
                    self.fast_forward = not self.fast_forward
        self.ff_label.update(delta)
        self.food_manager.update(self.snake.body)
        status = self.snake.update(delta * (3 ** self.fast_forward), self.food_manager)
        if len(self.snake.body) == LENGTH * HEIGHT:
            return COMMAND_WIN
        if status == COMMAND_LOSE:
            return status
        return

    def draw(self, surf):
        self.board.draw(surf)
        self.snake.draw(surf)
        self.food_manager.draw(surf)
        if self.fast_forward:
            self.ff_label.draw(surf, centered=False)
