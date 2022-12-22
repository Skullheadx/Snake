from game import Game
from game_over import GameOver
from help import Help
from menu import Menu
from setup import *

is_running = True
delta = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode(dimensions)
scene = Menu()

while is_running:

    status = scene.update(delta)
    if status == COMMAND_EXIT:
        is_running = False
    elif status == COMMAND_LOSE:
        scene = GameOver(len(scene.snake.body), win=False)
    elif status == COMMAND_WIN:
        scene.draw(screen)
        scene = GameOver(len(scene.snake.body), win=True)
    elif status == COMMAND_START:
        scene = Game()
    elif status == COMMAND_HELP:
        scene = Help()
    elif status == COMMAND_MENU:
        scene = Menu()

    scene.draw(screen)

    pygame.display.flip()
    delta = clock.tick(60)

pygame.quit()
