# This Python file uses the following encoding: utf-8

import pygame

class Timer():
    _clock = None
    dt:float = 0.16
    def __init__(self):
        self._clock = pygame.time.Clock()
    def update(self):
        self.dt = self._clock.tick(60)/1000

class Object:
    x = 0.0
    y = 0.0
    w = 0.0
    h = 0.0
    def__init__(self,x=0,y=0,w=0,h=0):
        _x = x
        _y = y
        _w = w
        _h = h
    def update(self,dt):
        pass
    def render(self):
        pass

class Ball(Object):
    _ball=None
    _wreckin_ball=None
    _ball_dir = [1,0]
    def__init__(self,x=320,y=240,w=30,h=30):
        super().__init__()
    def render (self):
        self.screen.fill([200,50,100],[320,240,30,30])
    def update(self,dt):
        if self.ball_dir[0] > 0 :
            self._x +=200

class Game:
    x= 0.0
    y=0.0
    _ball=None
    _wreckin_ball=None
    def __init__(self):
        pygame.init()
        self.game_init()
        self.timer = Timer()
        pass
    def game_init(self):
        self.size = self.width, self.height = 640,480
        self.black = 0,0,0
        self.white = 255,255,255

        self.screen= pygame.display.set_mode(self.size)

        self._ball = 200,39,150

        self.screen = pygame.display.set_mode(self.size)
    def loop(self):
        self.timer.update()

        self.keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        if self.keystate[pygame.K_d]:
            self.x += 100 * self.timer.dt
        if self.keystate[pygame.K_a]:
            self.x -= 100 * self.timer.dt
        if self.keystate[pygame.K_s]:
            self.y += 100 * self.timer.dt
        if self.keystate[pygame.K_w]:
            self.y -= 100 * self.timer.dt

        self.render()

    def render(self):
        self.screen.fill(self.black)


        self.screen.fill(self.white,[self.x,self.y,100,100])

        pygame.display.flip()

    def close(self):
        pygame.quit()
