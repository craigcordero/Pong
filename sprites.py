import pygame as pg
import random
import math
from settings import *


class paddle1(pg.sprite.Sprite):
                 #class.  #method

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(PADDLE_COLOR)
        self.rect = self.image.get_rect()
                        # gets the hit box
        self.rect.x = 5
        self.rect.y = HEIGHT / 2

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

class ball(pg.sprite.Sprite):

    def __init__(self, pong):
        pg.sprite.Sprite.__init__(self)

        self.pong = pong
        self.image = pg.Surface((BALL_WIDTH, BALL_HEIGHT))
        self.image.fill(BALL_COLOR)
        self.rect = self.image.get_rect()

        self.speedy = 10

        self.speedx = 10

    def update(self):

        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

        if self.rect.y > HEIGHT:
            self.speedy = -10

        if self.rect.y < 0:
            self.speedy = 10

        self.hit = pg.sprite.spritecollide(self, self.pong.paddlesprites, False)
                                    # ball                      # true = dead paddle
        if self.hit:

            if self.speedx == 10:
                self.speedx = -10
                return
            if self.speedx == -10:
                self.speedx = 10
                return




























