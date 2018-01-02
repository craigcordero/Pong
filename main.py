
from settings import *
from sprites import *

class Pong:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode ((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True


    def new(self):
        self.ball1 = ball(self)
        self.player2 = paddle2()
        self.player1 = paddle1()

        self.paddlesprites = pg.sprite.Group()
        self.paddlesprites.add(self.player1)
        self.paddlesprites.add(self.player2)

        self.ballsprites = pg.sprite.Group()
        self.ballsprites.add(self.ball1)

        self.run()

    def run(self):
        self.playing = True
        while self.playing == True:
            self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw()

    def update(self):
        self.clock.tick(FPS)
        self.paddlesprites.update()
        self.ballsprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing == True:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BACKGROUND)
        pg.draw.line(self.screen, (255, 255, 255), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 3)
        self.paddlesprites.draw(self.screen)
        self.ballsprites.draw(self.screen)
        #top left of image is (0,0)
        pg.display.flip()


P = Pong()

while P.running == True:
       #p.running: is same as above
    P.new()

#pg.QUIT
