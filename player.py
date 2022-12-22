from setup import *


class Player:
    move_time = 400  # ms
    min_time = 100
    time_decrease = 4

    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.time = 0
        self.body = [Body(self.position), Body(self.position - x_unit), Body(self.position - 2 * x_unit)]
        # self.body = [Body(self.position - i * x_unit) for i in range(64)]
        self.direction = None
        self.head = self.body[0]
        self.neck = self.body[1]

    def get_input(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            if not self.neck.collide_point(mod(self.position - y_unit)):
                self.direction = "up"
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if not self.neck.collide_point(mod(self.position + y_unit)):
                self.direction = "down"
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if not self.neck.collide_point(mod(self.position - x_unit)):
                self.direction = "left"
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if not self.neck.collide_point(mod(self.position + x_unit)):
                self.direction = "right"

    def update(self, delta, food_manager):
        if self.direction is None:
            return
        if self.time >= self.move_time:
            self.time -= self.move_time
            moved = True
            match self.direction:
                case "left":
                    self.position = mod(self.position - x_unit)
                case "right":
                    self.position = mod(self.position + x_unit)
                case "up":
                    self.position = mod(self.position - y_unit)
                case "down":
                    self.position = mod(self.position + y_unit)
                case _:
                    moved = False
            if moved:
                eaten = self.eaten_food(food_manager.food_list)
                if eaten is not None:
                    self.eat(food_manager, eaten)
                else:
                    self.move()
            for part in self.body:
                if part == self.head:
                    continue
                if self.head.is_colliding(part):
                    return COMMAND_LOSE
        self.time += delta

    def eaten_food(self, food_list):
        for food in food_list:
            if food.position == self.position:
                return food
        return None

    def update_head(self):
        self.head = self.body[0]
        self.neck = self.body[1]

    def eat(self, food_manager, food):
        self.body.insert(0, Body(self.position))
        food_manager.update(self.body)
        food_manager.food_list.remove(food)
        food_manager.add_food()
        self.update_head()
        self.move_time = max(self.min_time, self.move_time - self.time_decrease)
        sounds["eat"].play()

    def move(self):
        del self.body[-1]

        self.position = mod(self.position)

        self.body.insert(0, Body(self.position))
        self.update_head()

    def draw(self, surf):
        for part in self.body:
            if part == self.head:
                part.draw_head(surf)
            else:
                part.draw(surf)


class Body:
    scale = 1
    border_radius = 2

    def __init__(self, position):
        self.position = position.copy()
        self.length, self.width = side_length * self.scale, side_length * self.scale

    def get_rect(self):
        return pygame.Rect(self.position.x + (1 - self.scale) * side_length / 2,
                           self.position.y + (1 - self.scale) * side_length / 2, self.length, self.width)

    def is_colliding(self, b):
        if self.get_rect().colliderect(b.get_rect()):
            return True
        return False

    def collide_point(self, pos):
        if self.position == pos:
            return True
        return False

    def draw(self, surf):
        pygame.draw.rect(surf, LIGHT_BLUE, self.get_rect(), border_radius=self.border_radius)
        pygame.draw.rect(surf, BLACK, self.get_rect(), width=3, border_radius=self.border_radius)

    def draw_head(self, surf):
        pygame.draw.rect(surf, DARK_BLUE, self.get_rect(), border_radius=self.border_radius)
        pygame.draw.rect(surf, BLACK, self.get_rect(), width=3, border_radius=self.border_radius)
