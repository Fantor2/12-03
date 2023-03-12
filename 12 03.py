import pygame as pg
import sys
from grass import Grass
from settings import *
from bar import Bar
import random

FPS=60
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000



def bar_spawn(bar.sprites, y):
    coord = [110,210,310,410]
    random.shuffle(coord)
    b = Bar(screen,coord[i],)
    bar_sprites.append(b)
    bar_sprites
pg.init()
screen= pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
grass = Grass("grass.png",screen , x, y)
bar_sprites[]
for i in range(3):
    bar_spawn(bar.sprites,i)
while True:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

grass.update()
screen_fill((0,0,0))
pg.display.update()
for i in range(len(bar_sprites)):
    bar_sprites[i].update()
    if bar_sprites[i].rect.y > SCREEN_HEIGHT:
        bar_sprites.pop(i)
        bar_sprites.append(b)



for i in range(len(bar_sprites)):
    bar_sprites[i].draw()
    
