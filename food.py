from setup import *


class Food:
    radius = side_length * 0.9 / 2
    image = pygame.transform.scale(pygame.image.load("assets/apple.png"), (side_length, side_length))

    def __init__(self, position):
        self.position = pygame.Vector2(position)

    def update(self, delta):
        pass

    def draw(self, surf):
        pygame.draw.circle(surf, RED, self.position + pygame.Vector2(side_length / 2, side_length / 2), self.radius)
        pygame.draw.circle(surf, BLACK, self.position + pygame.Vector2(side_length / 2, side_length / 2),
                           self.radius, width=3)
        # surf.blit(self.image,self.position)
