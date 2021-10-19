from pico2d import *

WINx = 1024
WINy = 600
moveWinx = 0
moveWiny = 0

character = load_image('MarioMove.png')
object_image = load_image('object.png')
map1 = load_image('1-1.png')

class hero:
    dir = 0
    herodir = 0
    status = 0
    speed = 0
    xspeed = 0
    xMAX = 14
    xa = 0.5
    frame = 0
    framedir = 0
    py = 0
    g = 40.0
    t = 0.0
    ga = 4.0

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
                    self.xspeed = 0
                elif event.key == SDLK_LEFT:
                    self.dir -= 1
                    self.frame = 0
                    self.framedir = 0
                    self.xspeed = 0
                elif event.key == SDLK_UP and self.status == 0:
                    self.py = self.y
                    self.status = 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_DOWN:
                    pass
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
            if self.status == 1:
                if self.y - self.py > 70:
                    if self.y - self.py > 170:
                        self.frame = 3
                    elif self.y - self.py > 110:
                        self.frame = 2
                    else:
                        self.frame = 1
                else:
                    self.frame = 0
            elif self.status == -1:
                if self.y - self.py < 50:
                    self.frame = 4

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
            self.y = -(self.ga/2) * (self.t ** 2) + self.g * self.t + self.py
            self.t += 1
            if (self.ga/2) * (self.t ** 2) > self.g * self.t:
                self.status = -1
        elif self.status == -1:
            self.y = -(self.ga / 2) * (self.t ** 2) + self.g * self.t + self.py
            self.t += 1
            if self.y < self.py:
                self.y = self.py
                self.status = 0
                self.t = 0
                self.frame = 0
            # 점프 구현

        self.x += self.dir * self.xspeed

        if self.dir == 0:
            self.xspeed -= self.xa*2
            if self.xspeed < 0:
                self.xspeed = 0
            self.x += self.herodir * self.xspeed
        else:
            self.xspeed += self.xa
            if self.xspeed > self.xMAX:
                self.xspeed = self.xMAX

    pass

class object:
    frame = 0
    fs = 0
    framedir = 0

    def __init__(self,x, y, ability = None):
        self.x = x
        self.y = y
        self.ability = ability

    def sprites(self):
        if self.ability == 0: # 코인
            object_image.clip_draw(self.frame * 24 + 5 + 96, 976 + 4, 15, 17, self.x, self.y, 30, 34)
            self.fs = self.fs + 1
            if self.fs == 3:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability == 1: # ?블럭
            object_image.clip_draw(self.frame * 24 + 4, 976 + 4, 16, 16, self.x, self.y, 32, 32)
            self.fs = self.fs + 1
            if self.fs == 5:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability == 2: # ?블럭 충돌
            object_image.clip_draw(self.frame * 24 + 4, 944 + 4, 16, 16, self.x, self.y, 32, 32)
            pass
        elif self.ability == 3:
            pass
        elif self.ability == 4:
            pass
        elif self.ability == 5:
            pass


    pass
class monster:
    frame = 0
    fs = 0
    framedir = 0

    def __init__(self, x, y, tribe):
        self.x = x
        self.y = y
        self.tribe = tribe

    def sprites(self):

        pass



    pass

def mapmove():
    global WINx
    global WINy
    global moveWinx
    global moveWiny
    global mario


    map_turn_s = 10


    if moveWinx < -(4222 * 2 + WINx):
        moveWinx = -(4222 * 2 + WINx)
    if moveWinx > 0:
        moveWinx = 0

    if moveWinx != 0 and mario.x < WINx * 3/5 and mario.dir == -1:
        if mario.x + mario.xMAX >= WINx * 3 / 5:
            moveWinx += mario.xspeed
        else:
            moveWinx += mario.xspeed*2
        mario.x += mario.xspeed*2
        if mario.x > WINx * 3/5:
            mario.x = WINx * 3/5

    if moveWinx != -(4222 * 2 + WINx) and mario.x > WINx * 2/5 and mario.dir == 1:
        if mario.x - mario.xMAX <= WINx * 2 / 5:
            moveWinx -= mario.xspeed
        else:
            moveWinx -= mario.xspeed*2
        mario.x -= mario.xspeed*2
        if mario.x < WINx * 2/5:
            mario.x = WINx * 2/5

    if moveWinx > 0:
        moveWinx = 0
    if moveWinx < -(4222 * 2 + WINx):
        moveWinx = -(4222 * 2 + WINx)

running = True

mario = hero(50, 60)
coin = object(200, 200, 0)
Qblock = object(150, 150, 1)


while running:
    clear_canvas()

    map1.clip_draw(0 ,0, 4222, 624, 2110*2.5 + moveWinx, 120 * 2.5 + moveWiny , 4224*2.5, 624*2.5)
    mario.sprites()

    # coin.sprites()
    # Qblock.sprites()

    update_canvas()

    mario.handle_events()
    mario.move()
    mapmove()

    delay(0.025)

close_canvas()

