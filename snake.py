import pygame as pg
from pygame.math import Vector2
import sys
# import the pciture of food and add it to the class and continue with the game
pg.init()
bg_color = (173, 204, 96)
size_of_cells = 25
num_of_cells = 20


screen = pg.display.set_mode((size_of_cells*num_of_cells, size_of_cells*num_of_cells))
pg.display.set_caption("SNAKE GAME")
clock = pg.time.Clock()

class Food:
    def __init__(self):
        self.position = Vector2(5, 6)
    def draw_food(self):
        food = pg.Rect(self.position.x * size_of_cells, self.position.y * size_of_cells, size_of_cells, size_of_cells)
        pg.draw.rect(screen, (30, 120, 130), food)


food = Food()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(bg_color)
    food.draw_food()
    pg.display.update()
    clock.tick(60)
