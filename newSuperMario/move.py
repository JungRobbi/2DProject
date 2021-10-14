from pico2d import *

class hero:
    dir = 0
    herodir = 0
    status = 0
    speed = 0
    xspeed = 8
    frame = 0
    framedir = 0
    py = 0
    g = 30.0
    t = 0.0
    ga = 2.0

    def __init__(self,x, y):
        self.x = x
        self.y = y
    def handle_events(self):
        global running

        self.events = get_events()
        for event in self.events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir += 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_LEFT:
                    self.dir -= 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_UP and self.status == 0:
                    self.py = self.y
                    self.status = 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_DOWN:
                    self.status = 0
                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                    self.herodir = 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
                    self.herodir = -1
        pass

    def sprites(self):
        if self.status != 0: # 점프 등의 특수 상태
           if self.dir == 0:  # 정지
               if self.herodir == 1:
                   character.clip_draw(self.frame * 32, 960 - 2 * 40, 32, 40, self.x, self.y, 64, 80)
               else:
                   character.clip_composite_draw(self.frame * 32, 960 - 2 * 40, 32, 40, 0, 'h', self.x, self.y, 64, 80)
           if self.dir == 1:
               character.clip_draw(self.frame * 32, 960 - 2 * 40, 32, 40, self.x, self.y, 64, 80)
           elif self.dir == -1:
               character.clip_composite_draw(self.frame * 32, 960 - 2 * 40, 32, 40, 0, 'h', self.x, self.y, 64, 80)
        else: # 기본 이동 스프라이트
           if self.dir == 0:  # 정지
               if self.herodir == 1:
                   character.clip_draw(self.frame * 32, 960 - 40, 32, 40, self.x, self.y, 64, 80)
               else:
                   character.clip_composite_draw(self.frame * 32, 960 - 40, 32, 40, 0, 'h', self.x, self.y, 64, 80)
           elif self.dir == 1:  # 오른쪽 걸음
               character.clip_draw(self.frame * 32, 960, 32, 40, self.x, self.y, 64, 80)
           elif self.dir == -1:  # 왼쪽 걸음
               character.clip_composite_draw(self.frame * 32, 960, 32, 40, 0, 'h', self.x, self.y, 64, 80)




        self.speed = (self.speed + 1) % 2


        if self.framedir == 0:
            self.frame = self.frame + self.speed
            if self.status == 1 or self.status == -1:
                if self.frame > 4:
                    self.frame = self.frame - self.speed
            elif self.dir == -1 or self.dir == 1:  # 나머지 프레임
                if self.frame >= 4:
                    self.framedir = 1
            elif self.dir == 0 and self.status == 0:
                if self.frame >= 9: # 정지 프레임
                    self.frame = 0
        else:
            self.frame = self.frame - self.speed
            if self.frame == 0:
                self.framedir = 0

    def move(self):
        if self.status == 1:
            self.y = -(self.ga/2)* (self.t ** 2) + self.g * self.t + self.py
            self.t += 1
            if self.y < self.py:
                self.y = self.py
                self.status = 0
                self.t = 0
            # 점프 구현

        self.x += self.dir * self.xspeed


    pass

def mapmove():
    global WINx
    global WINy
    global moveWinx
    global moveWiny
    global mario
    global space


    map_turn_s = 10


    if moveWinx < -(4222 * 2 + WINx):
        moveWinx = -(4222 * 2 + WINx)
    if moveWinx > 0:
        moveWinx = 0

    if moveWinx != 0 and mario.x < WINx * 3/5and mario.dir == -1:
        moveWinx += mario.xspeed*3
        mario.x += mario.xspeed*3
        if mario.x > WINx * 3/5:
            mario.x = WINx * 3/5

    if moveWinx != -(4222 * 2 + WINx) and mario.x > WINx * 2/5and mario.dir == 1:
        moveWinx -= mario.xspeed*3
        mario.x -= mario.xspeed*3
        if mario.x < WINx * 2/5:
            mario.x = WINx * 2/5





    if moveWinx > 0:
        moveWinx = 0
    if moveWinx < -(4222 * 2 + WINx):
        moveWinx = -(4222 * 2 + WINx)





WINx = 1024
WINy = 600
moveWinx = 0
moveWiny = 0
xa = 0
space = 1

open_canvas(WINx, WINy)

character = load_image('MarioMove.png')
map1 = load_image('1-1.png')

running = True

mario = hero(50, 60)

while running:
    clear_canvas()

    map1.clip_draw(0 ,0, 4222, 624, 2110*2.5 + moveWinx, 120 * 2.5 + moveWiny , 4224*2.5, 624*2.5)
    mario.sprites()

    update_canvas()

    mario.handle_events()
    mario.move()
    mapmove()

    delay(0.025)

close_canvas()


