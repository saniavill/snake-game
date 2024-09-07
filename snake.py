import pygame as pg
from pygame.math import Vector2
import sys
import random
# import the picture of food and add it to the class and continue with the game
pg.init()
font = pg.font.Font("Coolvetica Rg.ttf", 45)
bg_color = (173, 204, 96)
size_of_cells = 25
num_of_cells = 20
border_width = 75

screen = pg.display.set_mode((2 * border_width + size_of_cells*num_of_cells, 2 * border_width + size_of_cells*num_of_cells))
pg.display.set_caption("SNAKE GAME")
clock = pg.time.Clock()


class Food:
    def __init__(self, snake_line):
        self.position = self.initial_position(snake_line)

    def draw_food(self):
        food = pg.Rect(border_width + self.position.x * size_of_cells, border_width + self.position.y * size_of_cells, size_of_cells, size_of_cells)
        #pg.draw.rect(screen, (30, 120, 130), food)
        screen.blit(food_surface, food)

    def random_cell(self):
        x = random.randint(0, num_of_cells - 1)
        y = random.randint(0, num_of_cells - 1)
        return Vector2(x, y)

    def initial_position(self, snake_line):
        position = self.random_cell()
        while position in snake_line:
            position = self.random_cell()
        return position


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 7), Vector2(5, 7)]
        self.direction = Vector2(1, 0)
        self.add_cell = False

    def draw_snake(self):
        for cell in self.body:
            one_cell = (border_width + cell.x * size_of_cells, border_width + cell.y * size_of_cells, size_of_cells, size_of_cells)
            pg.draw.rect(screen, (63, 174, 211), one_cell, 0, 7)

    def update_pos(self):
        if self.add_cell == True:
            self.body.insert(0, self.body[0] + self.direction)
            self.add_cell = False
        else:
            self.body = self.body[:-1]
            self.body.insert(0, self.body[0] + self.direction)

    def reset_pos(self):
        self.body = [Vector2(6, 7), Vector2(5, 7)]
        self.direction = Vector2(1, 0)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.pause = "running"

    def draw_objects(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def update(self):
        if self.pause == "running":
            self.snake.update_pos()
            self.is_food_eaten()
            self.is_snake_in_the_window()
            self.is_head_touching_tail()

    def is_food_eaten(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.initial_position(self.snake.body)
            self.snake.add_cell = True

    def is_snake_in_the_window(self):
        if self.snake.body[0].x == num_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == num_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def is_head_touching_tail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def game_over(self):
        self.snake.reset_pos()
        self.food.position = self.food.initial_position(self.snake.body)
        self.pause = "paused"


game_loop = Game()
food_surface = pg.transform.scale(pg.image.load('Chick.png'), (35, 35))
update = pg.USEREVENT
pg.time.set_timer(update, 200)

while True:
    for event in pg.event.get():
        if event.type == update:
            game_loop.update()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if game_loop.pause == 'paused':
                game_loop.pause = 'running'
            if event.key == pg.K_UP and game_loop.snake.direction != Vector2(0, 1):
                game_loop.snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN and game_loop.snake.direction != Vector2(0, -1):
                game_loop.snake.direction = Vector2(0, 1)
            if event.key == pg.K_RIGHT and game_loop.snake.direction != Vector2(-1, 0):
                game_loop.snake.direction = Vector2(1, 0)
            if event.key == pg.K_LEFT and game_loop.snake.direction != Vector2(1, 0):
                game_loop.snake.direction = Vector2(-1, 0)

    # drawings
    screen.fill(bg_color)
    pg.draw.rect(screen, (0, 0, 0), (border_width-5, border_width-5, size_of_cells*num_of_cells + 10, size_of_cells*num_of_cells + 10), 5)
    game_loop.draw_objects()
    font_render = font.render("SNAKE", True, (0, 0, 0))
    screen.blit(font_render, (border_width-5, 20))
    pg.display.update()
    clock.tick(60)
