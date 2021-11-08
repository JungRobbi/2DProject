from pico2d import *

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
    g = 4.5
    ga = 0.05
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
            self.y += self.g
            self.g = self.g - self.ga
            if self.g <= 0:
                self.status = -1
        elif self.status == -1: # 하강
            self.y -= self.g
            self.g = self.g + self.ga
            if self.y < self.py:
                self.y = self.py
                self.status = 0
                self.g = 4.5
                self.frame = 0
            # 점프 구현

        if self.sit != 1: # 앉기 제외
            self.x += self.dir * self.xspeed

            if self.dir == 0:
                self.xspeed -= self.xa * 3
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


    def contact_check(self, obj):
        Qblock_sizex = 16
        Qblock_sizey = 16

        if self.grow == 0:
            if (self.x - 16 <= obj.x + (14.4)) and (
                    self.x + 16 >= obj.x - (14.4)) and (
                    self.y - 32 <= obj.y + (12.8)) and (
                    self.y + 8 >= obj.y - (16) and (
                    obj.ability >= 300 and obj.ability < 400
            )):
                if obj.ability == 300:
                    self.grow = 1
                    obj.ability = -1

            elif (self.x - 16 <= obj.x + (Qblock_sizex)) and (
                    self.x + 16 >= obj.x - (Qblock_sizex)) and (
                    self.y - 32 <= obj.y + (Qblock_sizey)) and (
                    self.y + 8 >= obj.y - (Qblock_sizey) and(
                obj.ability < 200
            )):

                self.x -= self.dir * self.xspeed
                if self.dir == 0:
                    self.x -= self.herodir * self.xspeed

                if self.status == 1:
                    self.y -= self.g
                    self.g = self.g + self.ga
                    self.status = -1
                elif self.status == -1:
                    self.py = obj.y + (Qblock_sizey) + 33
                    self.y = self.py
                    self.status = 0
                    self.g = 4.5
                    self.t = 0
                    self.frame = 0


            elif (self.x - 16 <= obj.x + (obj.size[0])) and (
                    self.x + 16 >= obj.x - (obj.size[0])) and (
                    self.y - 32 <= obj.y + (obj.size[1])) and (
                    self.y + 8 >= obj.y - (obj.size[1]) and(
                obj.ability == 999  # ground
            )):
                self.x -= self.dir * self.xspeed
                if self.dir == 0:
                    self.x -= self.herodir * self.xspeed

                if self.status == 1:
                    self.status = -1
                elif self.status == -1:
                    self.py = obj.y + (obj.size[1]) + 33
                    self.y = self.py
                    self.status = 0
                    self.g = 4.5
                    self.t = 0
                    self.frame = 0







