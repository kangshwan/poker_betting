import pygame as pg
import point_n_rect as pnr
import poker_hands as pkhand

pg.init()

TABLE = (  0,128,  0)
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
BROWN = (150, 75,  0)

size  = [1280,960]
screen = pg.display.set_mode(size)
pg.display.set_caption("Poker Game")

done = False
clock = pg.time.Clock()

test = pnr.Point(2,3)
class Player:
    # in player class, draw
    pass

while not done:
    # This limits the while loop to a max of 30 time per second
    # 30fps
    clock.tick(30)
    # Main Event Loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(type(pg.mouse.get_pos()))
    screen.fill(WHITE)
    pg.draw.rect(screen, TABLE,[0,460,1280,500])
    pg.draw.rect(screen, BROWN,[0,410,1280,50])
    # This MUST happen after all the other drawing commands
    pg.display.update()
pg.quit()

