from pico2d import *
from Map_def import *

#hero
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

moveWinx = 0
moveWiny = 0

class hero:
    image = None
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
    sit = 0


    def __init__(self,x, y):
        self.x = x
        self.y = y
        if hero.image == None:
            hero.image = load_image('MarioMove.png')



    def update(self):

        if self.status == 1 or self.status == -1:
            fs_deel = 7
        elif self.status >= 99:
            fs_deel = 8
        elif self.sit == 1:
            fs_deel = 15
        elif self.dir == -1 or self.dir == 1:
            if self.xspeed == 3.0:
                fs_deel = 6
            else:
                fs_deel = 4
        elif self.dir == 0:
            fs_deel = 8


                    # 프레임
        if self.grow == 1: # 성장 후
            if self.framedir == 0:
                if self.fs == fs_deel:
                    self.frame = self.frame + 1
                    if self.sit == 1 and self.status == -1:
                        if self.status + 1 == 0:
                            self.frame = 0

                if self.status == 1 or self.status == -1:
                    if self.frame > 19:
                        self.frame = 19
                elif self.status >= 99:
                    if self.status == 199:
                        self.status = 0
                    elif self.frame > 12:
                        self.frame = 0

                elif self.sit == 1 and self.status == 0:
                    if self.frame >= 3:
                        self.frame = 2

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

        elif self.grow == 0: # 성장 전
            if self.framedir == 0:
                if self.fs == fs_deel:
                    self.frame = self.frame + 1
                    if self.sit == 1 and self.status == -1:
                        if self.status + 1 == 0:
                            self.frame = 0

                if self.status == 1 or self.status == -1:
                    if self.frame > 20:
                        self.frame = 20
                elif self.sit == 1 and self.status == 0:
                    if self.frame >= 3:
                        self.frame = 2

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
            if self.status == 1 or self.status == -1:  # 점프

                if self.dir == 0:  # 정지
                    if self.herodir == 1:
                        self.image.clip_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                elif self.dir == 1:
                    self.image.clip_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, self.x, self.y, self.size[0],
                                          self.size[1])
                elif self.dir == -1:
                    self.image.clip_composite_draw(self.frame * 32, 1000 - 4 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                    self.size[0], self.size[1])
            elif self.status == 99: # 죽음
                self.image.clip_draw(self.frame * 32, 1000 - 7 * 40, 32, 40, self.x, self.y, self.size[0],
                                      self.size[1])

            else:  # 기본 이동 스프라이트
                if self.sit == 1:
                    if self.herodir == 1:
                        self.image.clip_draw(self.frame * 32, 1000 - 5 * 40, 32, 40, self.x, self.y, self.size[0],
                                          self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 5 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])

                elif self.dir == 0:  # 정지
                    if self.herodir == 1:
                        self.image.clip_draw(self.frame * 32, 1000 - 1 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 1 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                elif self.dir == 1:  # 오른쪽 걸음
                    if self.xspeed == 3.0:
                        self.image.clip_draw(self.frame * 32, 1000 - 3 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        self.image.clip_draw(self.frame * 32, 1000 - 2 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                elif self.dir == -1:  # 왼쪽 걸음
                    if self.xspeed == 3.0:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 3 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 2 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
        elif self.grow == 0: # 성장 전
            if self.status == 1 or self.status == -1:  # 점프
                if self.dir == 0:  # 정지
                    if self.herodir == 1:
                        self.image.clip_draw(self.frame * 32, 1000 - 18 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 18 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                elif self.dir == 1:
                    self.image.clip_draw(self.frame * 32, 1000 - 18 * 40, 32, 40, self.x, self.y, self.size[0],
                                          self.size[1])
                elif self.dir == -1:
                    self.image.clip_composite_draw(self.frame * 32, 1000 - 18 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                    self.size[0], self.size[1])
            else:  # 기본 이동 스프라이트
                if self.sit == 1:
                    if self.herodir == 1:
                        self.image.clip_draw(self.frame * 32, 1000 - 19 * 40, 32, 40, self.x, self.y, self.size[0],
                                          self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 19 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])

                elif self.dir == 0:  # 정지
                    if self.herodir == 1:
                        self.image.clip_draw(self.frame * 32, 1000 - 15 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 15 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                elif self.dir == 1:  # 오른쪽 걸음
                    if self.xspeed == 3.0:
                        self.image.clip_draw(self.frame * 32, 1000 - 17 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                    else:
                        self.image.clip_draw(self.frame * 32, 1000 - 16 * 40, 32, 40, self.x, self.y, self.size[0],
                                              self.size[1])
                elif self.dir == -1:  # 왼쪽 걸음
                    if self.xspeed == 3.0:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 17 * 40, 32, 40, 0, 'h', self.x, self.y,
                                                        self.size[0], self.size[1])
                    else:
                        self.image.clip_composite_draw(self.frame * 32, 1000 - 16 * 40, 32, 40, 0, 'h', self.x, self.y,
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

        if self.sit != 1: # 앉기 제외
            self.x += self.dir * self.xspeed

            if self.dir == 0:
                self.xspeed -= self.xa * 2
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
    global moveWinx, moveWiny
    image = None
    frame = 0
    fs = 0
    framedir = 0

    def __init__(self, x, y, ability=None):
        self.x = x
        self.y = y
        self.ability = ability
        if object.image == None:
            object.image = load_image('object.png')

    def draw(self):
        if self.ability == 0:  # 코인
            self.image.clip_draw(self.frame * 24 + 96, 1000 - 24, 24, 24, self.x + moveWinx, self.y + moveWiny, 48,
                                   48)
            self.fs = self.fs + 1
            if self.fs == 20:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 100 and self.ability <= 110:  # ?블럭
            self.image.clip_draw(self.frame * 24, 1000 - 24, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 30:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 111 and self.ability <= 120:  # ?블럭 충돌
            self.image.clip_draw(self.frame * 24, 1000 - 24 * 2, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 10:
                self.fs = 0
                # self.ability = 99
                self.frame = (self.frame + 1) % 8

        elif self.ability == 2:  # 일반 벽돌
            self.image.clip_draw(0, 1000 - 24 * 3, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

        elif self.ability == 3:  # 빛나는 벽돌(코인 벽돌)
            self.image.clip_draw(self.frame * 24, 1000 - 24 * 3, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 20:
                self.fs = 0
                self.frame = (self.frame + 1) % 4

        elif self.ability == 4:  # 표정 벽돌 - 1
            self.image.clip_draw(0 * 24, 1000 - 24 * 4, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

        elif self.ability == 5:  # 표정 벽돌 - 2
            self.image.clip_draw(1 * 24, 1000 - 24 * 4, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 150:
                self.fs = 0
                self.ability = 5

        elif self.ability == 98:
            # 철 블럭 (아무효과 X)
            self.image.clip_draw(9 * 24, 1000 - 24 * 2, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)

        elif self.ability == 99:
            # 아이템 블럭 사용 후 블럭 (아무효과 X)
            self.image.clip_draw(8 * 24, 1000 - 24 * 2, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)


class object_item:
    global moveWinx, moveWiny
    image = None
    dir = 1

    def __init__(self, x, y, ability=None):
        self.x = x
        self.y = y
        self.ability = ability
        if object_item.image == None:
            object_item.image = load_image('object.png')

        if self.ability == 3:
            self.status = 1
            self.ga = 0.1
            self.g = 6.0
            self.t = 0
            self.py = self.y

    def draw(self):
        if self.ability == 0:  # 일반 버섯
            self.image.clip_draw(0, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)
        elif self.ability == 1:  # 특수 버섯
            self.image.clip_draw(40 * 1, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)
        elif self.ability == 2:  # 꽃
            self.image.clip_draw(40 * 2, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)
        elif self.ability == 3:  # 별
            self.image.clip_draw(40 * 3, 0, 40, 40, self.x + moveWinx, self.y + moveWiny, 32, 32)

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
    global moveWinx, moveWiny
    image = None
    frame = 0
    fs = 0
    framedir = 0

    def __init__(self, x, y, tribe):
        self.x = x
        self.y = y
        self.tribe = tribe
        if monster.image == None:
            monster.image = load_image('Monster.png')

    def draw(self):
        if self.tribe == 0:  # 굼바
            self.image.clip_draw(self.frame * 24, 1000 - 24, 24, 24, self.x + moveWinx, self.y + moveWiny, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 18:
                self.fs = 0
                self.frame = (self.frame + 1) % 9

