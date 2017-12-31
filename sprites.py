import pygame as pg
from settings import *


class paddle1(pg.sprite.Sprite):
                 #class.  #method

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(PADDLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 250

    def keypress(self):
        self.keys = pg.key.get_pressed()

        if self.keys[pg.K_w] == True:
            self.rect.y = self.rect.y - PADDLE_SPEED

        if self.keys[pg.K_s] == True:
            self.rect.y = self.rect.y + PADDLE_SPEED


    def update(self):
        self.keypress()



class paddle2(pg.sprite.Sprite):
                 # class.  #method

     def __init__(self):
         pg.sprite.Sprite.__init__(self)
         self.image = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
         self.image.fill(PADDLE_COLOR)
         self.rect = self.image.get_rect()
         self.rect.x = WIDTH - PADDLE_WIDTH - 5
         self.rect.y = HEIGHT / 2


     def keypress(self):
        self.keys = pg.key.get_pressed()

        if self.keys[pg.K_e] == True:
                self.rect.y = self.rect.y - PADDLE_SPEED

        if self.keys[pg.K_d] == True:
            self.rect.y = self.rect.y + PADDLE_SPEED


     def update(self):
        self.keypress()




