import random

from food import Food
from setup import *


class FoodManager:

    def __init__(self):
        # self.food_list = [Food(center + pygame.Vector2(2 * side_length, 0))]
        self.food_list = [Food(center + pygame.Vector2(1 * side_length, 0))]
        self.taken = set()
        self.poll = [(i * side_length, j * side_length) for i in range(LENGTH) for j in range(HEIGHT)]

    def is_taken(self, pos, poll):
        poll.remove(pos)
        if pos in self.taken:
            return True
        return False

    def add_food(self):
        poll = self.poll[:]
        while len(poll) > 0:
            pos = random.choice(poll)

            if not self.is_taken(pos, poll):
                self.food_list.append(Food(pos))
                return

    def update(self, body):
        self.taken = set()
        for i in body:
            self.taken.add(tuple(i.position))

    def draw(self, surf):
        for food in self.food_list:
            food.draw(surf)
