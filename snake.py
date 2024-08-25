import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("SNAKE GAME")
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    clock.tick(60)
