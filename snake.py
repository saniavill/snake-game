import pygame as pg
from pygame.math import Vector2
import sys
import random
# import the picture of food and add it to the class and continue with the game
pg.init()
bg_color = (173, 204, 96)
size_of_cells = 25
num_of_cells = 20


screen = pg.display.set_mode((size_of_cells*num_of_cells, size_of_cells*num_of_cells))
pg.display.set_caption("SNAKE GAME")
clock = pg.time.Clock()

class Food:
    def __init__(self):
        self.position = self.initial_position()

    def draw_food(self):
        food = pg.Rect(self.position.x * size_of_cells, self.position.y * size_of_cells, size_of_cells, size_of_cells)
        #pg.draw.rect(screen, (30, 120, 130), food)
        screen.blit(food_surface, food)

    def initial_position(self):
        x = random.randint(0, num_of_cells - 1)
        y = random.randint(0, num_of_cells - 1)
        position = Vector2(x, y)
        return position

class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for cell in self.body:
            one_cell = (cell.x * size_of_cells, cell.y * size_of_cells, size_of_cells, size_of_cells)
            pg.draw.rect(screen, (63, 174, 211), one_cell, 0, 7)

    def update_pos(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)


class Game:
    pass


food = Food()
snake = Snake()
food_surface = pg.transform.scale(pg.image.load('Chick.png'), (35, 35))
update = pg.USEREVENT
pg.time.set_timer(update, 200)

while True:
    for event in pg.event.get():
        if event.type == update:
            snake.update_pos()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and snake.direction != Vector2(0, 1):
                snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN and snake.direction != Vector2(0, -1):
                snake.direction = Vector2(0, 1)
            if event.key == pg.K_RIGHT and snake.direction != Vector2(-1, 0):
                snake.direction = Vector2(1, 0)
            if event.key == pg.K_LEFT and snake.direction != Vector2(1, 0):
                snake.direction = Vector2(-1, 0)

    # drawings
    screen.fill(bg_color)
    food.draw_food()
    snake.draw_snake()
    pg.display.update()
    clock.tick(60)
