from pico2d import *
import game_framework
import Title_state


WINx = 1024
WINy = 600
moveWinx = 0
moveWiny = 0
stage = 1

Mario_image = None
object_image = None
Monster_image = None
map1 = None
map2 = None

mario = None
#block
coin = []
Qblock = []
brick = []
skbrick = []
Steelblock = []

#item
item = []

#monster
goomba = []

class hero:
    dir = 0
    herodir = 1
    status = 0
    xspeed = 0
    xMAX = 3.0
    xa = 0.01
    frame = 0
    fs = 0
    framedir = 0
    py = 0
    g = 6.0
    t = 0.0
    ga = 0.1
    size = [64, 80]
    grow = 0


    def __init__(self,x, y):
        self.x = x
        self.y = y

    def update(self):

        if self.status != 0:
            fs_deel = 7
        elif self.dir == -1 or self.dir == 1:
            if self.xspeed == 3.0:
                fs_deel = 6
            else:
                fs_deel = 4
        elif self.dir == 0:
            fs_deel = 8


                    # 프레임
        if self.grow == 1:
            if self.framedir == 0:
                if self.fs == fs_deel:
                    self.frame = self.frame + 1
                if self.status != 0:
                    if self.frame > 19:
                        self.frame = 19

                elif self.dir == -1 or self.dir == 1:  # 나머지 프레임
                    if self.frame > 10 and self.xspeed == 3.0:
                        self.frame = 0
                        self.framedir = 0

                    if self.frame > 27:
                        self.frame = 4
                        self.framedir = 0
                elif self.dir == 0 and self.status == 0:
                    if self.frame > 22:  # 정지 프레임
                        self.frame = 22
                        self.framedir = 1
            else:
                if self.fs == fs_deel:
                    self.frame = self.frame - 1
                if self.frame <= 0:
                    self.frame = 0
                    self.framedir = 0
        elif self.grow == 0:
            if self.framedir == 0:
                if self.fs == fs_deel:
                    self.frame = self.frame + 1
                if self.status != 0:
                    if self.frame > 20:
                        self.frame = 20

                elif self.dir == -1 or self.dir == 1:  # 나머지 프레임
                    if self.frame > 9 and self.xspeed == 3.0:
                        self.frame = 0
                        self.framedir = 0

                    if self.frame > 22:
                        self.frame = 0
                        self.framedir = 0
                elif self.dir == 0 and self.status == 0:
                    if self.frame > 20:  # 정지 프레임
                        self.frame = 0
                        self.framedir = 0
            else:
                if self.fs == fs_deel:
                    self.frame = self.frame - 1
                if self.frame <= 0:
                    self.frame = 0
                    self.framedir = 0




        self.fs = self.fs + 1
        if self.fs > fs_deel:
            self.fs = 0
                # 이동
        self.move()

    def draw(self):

        if self.grow == 1: # 성장 후
            if self.status != 0:  # 점프 등의 특수 상태
                if self.dir == 0:  # 정지
                    if self.herodir == 1:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                if self.dir == 1:
                    Mario_image.clip_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, self.x, self.y, self.size[0],
                                          self.size[1])
                elif self.dir == -1:
                    Mario_image.clip_composite_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                    self.size[0], self.size[1])
            else:  # 기본 이동 스프라이트
                if self.dir == 0:  # 정지
                    if self.herodir == 1:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 1 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 1 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                elif self.dir == 1:  # 오른쪽 걸음
                    if self.xspeed == 3.0:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 3 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 2 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                elif self.dir == -1:  # 왼쪽 걸음
                    if self.xspeed == 3.0:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 3 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                    else:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 2 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
        elif self.grow == 0: # 성장 전
            if self.status != 0:  # 점프 등의 특수 상태
                if self.dir == 0:  # 정지
                    if self.herodir == 1:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 11 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 11 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                if self.dir == 1:
                    Mario_image.clip_draw(self.frame * 32, 1000 - 11 * 40, 32, 40, self.x, self.y, self.size[0],
                                          self.size[1])
                elif self.dir == -1:
                    Mario_image.clip_composite_draw(self.frame * 32, 1000 - 11 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                    self.size[0], self.size[1])
            else:  # 기본 이동 스프라이트
                if self.dir == 0:  # 정지
                    if self.herodir == 1:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 8 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 8 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                elif self.dir == 1:  # 오른쪽 걸음
                    if self.xspeed == 3.0:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 10 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        Mario_image.clip_draw(self.frame * 32, 1000 - 9 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                elif self.dir == -1:  # 왼쪽 걸음
                    if self.xspeed == 3.0:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 10 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                    else:
                        Mario_image.clip_composite_draw(self.frame * 32, 1000 - 9 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])

    def move(self):
        if self.status == 1: # 상승
            self.y = -(self.ga/2) * (self.t ** 2) + self.g * self.t + self.py
            self.t += 0.7
            if (self.ga/2) * (self.t ** 2) > self.g * self.t:
                self.status = -1
        elif self.status == -1: # 하강
            self.y = -(self.ga / 2) * (self.t ** 2) + self.g * self.t + self.py
            self.t += 0.7
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
            if self.xspeed < self.xMAX:
                self.xspeed += self.xa
            elif self.xspeed > self.xMAX:
                self.xspeed = self.xMAX
                self.frame = 0
                # x 이동

class object:
    global moveWinx; global moveWiny

    frame = 0
    fs = 0
    framedir = 0

    def __init__(self,x, y, ability = None):
        self.x = x
        self.y = y
        self.ability = ability

    def draw(self):
        if self.ability == 0: # 코인
            object_image.clip_draw(self.frame * 24 + 96, 1000 - 24, 24, 24, self.x + moveWinx, self.y + moveWiny , 48, 48)
            self.fs = self.fs + 1
            if self.fs == 20:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 100 and self.ability <= 110: # ?블럭
            object_image.clip_draw(self.frame * 24, 1000 - 24, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 30:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 111 and self.ability <= 120: # ?블럭 충돌
            object_image.clip_draw(self.frame * 24, 1000 - 24*2, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 10:
                self.fs = 0
                #self.ability = 99
                self.frame = (self.frame + 1) % 8

        elif self.ability == 2: # 일반 벽돌
            object_image.clip_draw(0, 1000 - 24 * 3, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

        elif self.ability == 3: # 빛나는 벽돌(코인 벽돌)
            object_image.clip_draw(self.frame * 24, 1000 - 24 * 3, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 20:
                self.fs = 0
                self.frame = (self.frame + 1) % 4

        elif self.ability == 4: # 표정 벽돌 - 1
            object_image.clip_draw(0 * 24, 1000 - 24 * 4, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

        elif self.ability == 5:  # 표정 벽돌 - 2
            object_image.clip_draw(1 * 24, 1000 - 24 * 4, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 150:
                self.fs = 0
                self.ability = 5

        elif self.ability == 98:
            # 철 블럭 (아무효과 X)
            object_image.clip_draw(9 * 24, 1000 - 24 * 2, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

        elif self.ability == 99:
            # 아이템 블럭 사용 후 블럭 (아무효과 X)
            object_image.clip_draw(8 * 24, 1000 - 24 * 2, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

class object_item:
    dir = 1

    def __init__(self, x, y, ability=None):
        self.x = x
        self.y = y
        self.ability = ability
        if self.ability == 3:
            self.status = 1
            self.ga = 0.1
            self.g = 6.0
            self.t = 0
            self.py = self.y

    def draw(self):
        if self.ability == 0:  # 일반 버섯
            object_image.clip_draw(0, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)
        elif self.ability == 1:  # 특수 버섯
            object_image.clip_draw(40 * 1, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)
        elif self.ability == 2:  # 꽃
            object_image.clip_draw(40 * 2, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)
        elif self.ability == 3:  # 별
            object_image.clip_draw(40 * 3, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)

    def move(self):
        if self.ability == 3:
            if self.status == 1:  # 상승
                self.y = -(self.ga / 2) * (self.t ** 2) + self.g * self.t + self.py
                self.t += 0.5
                if (self.ga / 2) * (self.t ** 2) > self.g * self.t:
                    self.status = -1
            elif self.status == -1:  # 하강
                self.y = -(self.ga / 2) * (self.t ** 2) + self.g * self.t + self.py
                self.t += 0.5
                if self.y < self.py:
                    self.y = self.py
                    self.status = 1
                    self.t = 0

        if self.ability != 2:
            self.x += self.dir * 0.9


class monster:
    frame = 0
    fs = 0
    framedir = 0

    def __init__(self, x, y, tribe):
        self.x = x
        self.y = y
        self.tribe = tribe

    def draw(self):
        if self.tribe == 0: # 굼바
            Monster_image.clip_draw(self.frame * 24, 1000 - 24, 24, 24, self.x + moveWinx, self.y + moveWiny , 48, 48)
            self.fs = self.fs + 1
            if self.fs == 18:
                self.fs = 0
                self.frame = (self.frame + 1) % 9

        pass

def enter(): # 생성
    global Mario_image, object_image, Monster_image, map1, map2, stage

    stage = 1
    mapcreate(stage)

    Mario_image = load_image('MarioMove.png')
    object_image = load_image('object.png')
    Monster_image = load_image('Monster.png')
    map1 = load_image('1-1.png')
    map2 = load_image('1-3.png')

def exit(): # 종료/제거
    global mario, coin, Qblock, brick, skbrick, Steelblock
    del (mario)
    del (coin)
    del (Qblock)
    del (brick)
    del (skbrick)
    del (Steelblock)

def handle_events():
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.framedir = 0
                mario.xspeed = 0
                if mario.herodir == 1:
                    mario.frame = 4
                else:
                    mario.frame = 0
            elif event.key == SDLK_LEFT:
                mario.dir -= 1
                mario.framedir = 0
                mario.xspeed = 0
                mario.frame = 0
                if mario.herodir == -1:
                    mario.frame = 4
                else:
                    mario.frame = 0
            elif event.key == SDLK_UP and mario.status == 0:
                mario.py = mario.y
                mario.status = 1
                mario.frame = 0
                mario.framedir = 0
            elif event.key == SDLK_DOWN:
                pass
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(Title_state)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                mario.dir -= 1
                mario.herodir = 1
            elif event.key == SDLK_LEFT:
                mario.dir += 1
                mario.herodir = -1

def update():
    mapmove()
    mario.update()

    for i in item:
        i.move()

    delay(0.001)

def draw():
    clear_canvas()
    if stage == 1:
        map1.clip_draw(0, 0, 4224, 624, 2110 * 2.5 + moveWinx, 120 * 2.5 + moveWiny, 4224 * 2.5, 624 * 2.5)
    elif stage == 2:
        map2.clip_draw(0, 0, 4224, 762, 2110 * 2.5 + moveWinx, 378 * 2.5 + moveWiny, 4224 * 2.5, 762 * 2.5)
    for c in coin:
        c.draw()
    for b in Qblock:
        b.draw()
    for b in brick:
        b.draw()
    for b in skbrick:
        b.draw()
    for b in Steelblock:
        b.draw()
    for i in item:
        i.draw()
    for m in goomba:
        m.draw()

    mario.draw()
    update_canvas()


def pause():
    pass

def resume():
    pass


def mapcreate(map):
    global mario, coin, Qblock, brick, skbrick, Steelblock
    global goomba

    if map == 1:
        ground1 = 65
        mario = hero(50, ground1)
        Qblock.append(object(48 * 12, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 15, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 15 + 32, ground1 + 60 * 2, 100))

        coin.append(object(48 * 22, ground1 + 60 * 1, 0))
        coin.append(object(48 * 22 + 32, ground1 + 60 * 1 + 32, 0))
        coin.append(object(48 * 22 + 32 * 2, ground1 + 60 * 1 + 32, 0))

        coin.append(object(48 * 26, ground1 + 60 * 2, 0))
        coin.append(object(48 * 26 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 26 + 32 * 2, ground1 + 60 * 2 + 32, 0))

        skbrick.append(object(48 * 29, ground1 + 60 * 4, 3))

        brick.append(object(48 * 35, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 35 + 32, ground1 + 60 * 2, 3))
        brick.append(object(48 * 35 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object(48 * 35 + 32, ground1 + 60 * 5, 100))

        coin.append(object(48 * 42, ground1 + 60 * 2, 0))
        coin.append(object(48 * 42 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 42 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 42 + 32 * 3, ground1 + 60 * 2, 0))

        coin.append(object(48 * 61, ground1 + 60 * 2, 0))
        coin.append(object(48 * 61 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 61 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 61 + 32 * 3, ground1 + 60 * 2, 0))

        brick.append(object(48 * 75, ground1 + 60 * 2, 2))
        Qblock.append(object(48 * 75 + 32, ground1 + 60 * 2, 100))
        brick.append(object(48 * 75 + 32 * 2, ground1 + 60 * 2, 2))

        Qblock.append(object(48 * 81, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 81 + 32, ground1 + 60 * 2, 100))

        coin.append(object(48 * 86, ground1 + 60 * 2, 0))
        coin.append(object(48 * 86 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 86 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 86 + 32 * 3, ground1 + 60 * 2, 0))

        coin.append(object(48 * 94, ground1 + 60 * 4, 0))
        coin.append(object(48 * 94 + 32, ground1 + 60 * 4 + 32, 0))
        coin.append(object(48 * 94 + 32 * 2, ground1 + 60 * 4 + 32, 0))
        Qblock.append(object(48 * 94 + 32 * 2, ground1 + 60 * 3, 100))
        Qblock.append(object(48 * 94 + 32 * 3, ground1 + 60 * 3, 101))
        Qblock.append(object(48 * 94 + 32 * 4, ground1 + 60 * 3, 100))
        brick.append(object(48 * 94 + 32 * 5, ground1 + 60 * 3, 2))
        brick.append(object(48 * 94 + 32 * 6, ground1 + 60 * 3, 2))

        brick.append(object(48 * 108 , ground1 + 60 * 2, 2))
        brick.append(object(48 * 108 + 32, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 108 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object(48 * 108 + 32 * 3, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 108 + 32 * 4, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 108 + 32 * 5, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 108 + 32 * 6, ground1 + 60 * 2, 100))
        brick.append(object(48 * 108 + 32 * 7, ground1 + 60 * 2, 2))
        brick.append(object(48 * 108 + 32 * 8, ground1 + 60 * 2, 2))

        Qblock.append(object(48 * 108 + 32 * 3, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object(48 * 108 + 32 * 4, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object(48 * 108 + 32 * 5, ground1 + 60 * 4 + 32, 100))

        skbrick.append(object(48 * 125, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 127, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 129, ground1 + 60 * 2, 2))

        coin.append(object(48 * 136, ground1 + 60 * 2, 0))
        coin.append(object(48 * 136 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 136 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 136 + 32 * 3, ground1 + 60 * 2, 0))

        Qblock.append(object(48 * 142, ground1 + 60 * 2, 102))

        brick.append(object(48 * 151 - 37, ground1 + 60 + 20 , 2))
        brick.append(object(48 * 151 - 5, ground1 + 60 + 20, 2))
        brick.append(object(48 * 151 + 27, ground1 + 60 + 20 , 2))
        brick.append(object(48 * 151 + 32 * 2 - 5, ground1 + 60 + 20 , 2))

        Qblock.append(object(48 * 156, ground1 + 60 * 4, 100))

        coin.append(object(48 * 162 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 162 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 162 + 32 * 3, ground1 + 60 * 2, 0))

        brick.append(object(48 * 175, ground1 + 60 * 2, 2))
        brick.append(object(48 * 175 + 32, ground1 + 60 * 2, 2))
        brick.append(object(48 * 175 + 32 * 2, ground1 + 60 * 2, 2))
        brick.append(object(48 * 175 + 32 * 3, ground1 + 60 * 2, 2))

        brick.append(object(48 * 189, ground1 + 60 * 2, 2))
        brick.append(object(48 * 189 + 32, ground1 + 60 * 2, 2))
        brick.append(object(48 * 189 + 32 * 2, ground1 + 60 * 2, 2))


        for k in range(8, 1, -1):
            for i in range(0,k):
                Steelblock.append(object(48 * 200 - 32 * i, ground1 + 32 * 8 - 32 * k - 10, 98))


        goomba.append(monster(48 * 10, ground1 - 10, 0))
        item.append(object_item(48 * 3, ground1 - 15, 0))
        item.append(object_item(48 * 4, ground1 - 15, 1))
        item.append(object_item(48 * 5, ground1 - 15, 2))
        item.append(object_item(48 * 6, ground1 - 15, 3))

    elif map == 2:
        mario = hero(50, 60)


def mapmove():
    global WINx
    global WINy
    global moveWinx
    global moveWiny
    global mario

    mapmax = -(4222 * 2 + WINx - 15)

    if moveWinx < mapmax:
        moveWinx = mapmax
    if moveWinx > 0:
        moveWinx = 0

    if moveWinx < 0 and mario.x < WINx * 3 / 5 and mario.dir == -1:
        if mario.x + mario.xMAX >= WINx * 3 / 5:
            moveWinx += mario.xspeed
        else:
            moveWinx += mario.xspeed*2
        mario.x += mario.xspeed*2
        if mario.x > WINx * 3 / 5:
            mario.x = WINx * 3 / 5

    if moveWinx > mapmax and mario.x > WINx * 2 / 5 and mario.dir == 1:
        if mario.x - mario.xMAX <= WINx * 2 / 5:
            moveWinx -= mario.xspeed
        else:
            moveWinx -= mario.xspeed*2
        mario.x -= mario.xspeed*2
        if mario.x < WINx * 2 / 5:
            mario.x = WINx * 2 / 5

    if moveWinx > 0:
        moveWinx = 0
    if moveWinx < mapmax:
        moveWinx = mapmax
        # 완료


