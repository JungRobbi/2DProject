from pico2d import *
import game_framework
import game_world
from object_variable import *

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 15

def contact_aAndb(a, b, p = 0):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if p == 3:
        if left_a > right_b: return 0
        if right_a < left_b: return 0
    else:
        if left_a > right_b: return 0
        if right_a < left_b: return 0
        if top_a < bottom_b: return 0
        if bottom_a > top_b: return 0

    if top_a - (a.g + 1.0) * game_framework.frame_time < bottom_b: return 1 # 아래에서 위로
    if bottom_a + (a.g + 1.0) * game_framework.frame_time > top_b: return 2 # 위에서 아래로

    return 3 # 좌,우

class object:
    image = None

    def __init__(self,x, y, ability = None):
        self.frame = 0
        self.fs = 0
        self.framedir = 0
        self.crex = x
        self.crey = y
        self.x = self.crex
        self.y = self.crey
        self.movex = 0
        self.movey = 0
        self.ability = ability
        if ability >= 0:
            self.size = [48, 48]
        if object.image == None:
            object.image = load_image('object.png')

    def update(self):
        if self.ability == 0:  # 코인
            self.fs = self.fs + 1
            if self.fs == 20:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 100 and self.ability <= 109:  # ?블럭
            self.fs = self.fs + 1
            if self.fs == 30:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 110 and self.ability <= 120:  # ?블럭 충돌
            self.fs = self.fs + 1
            if self.fs == 6:
                self.fs = 0
                self.frame = self.frame + 1
                if self.frame >= 7:
                    self.ability = 99
                    self.frame = 0
        elif self.ability == 3:  # 빛나는 벽돌(코인 벽돌)
            self.fs = self.fs + 1
            if self.fs == 20:
                self.fs = 0
                self.frame = (self.frame + 1) % 4

        elif self.ability == 5:  # 표정 벽돌 - 2
            self.fs = self.fs + 1
            if self.fs == 150:
                self.fs = 0
                self.ability = 5
        self.x = self.crex + self.movex
        self.y = self.crey + self.movey

    def draw(self):
        if self.ability == 0: # 코인
            self.image.clip_draw(self.frame * 24 + 96, 1000 - 24, 24, 24, self.x, self.y , self.size[0], self.size[1])

        elif self.ability >= 100 and self.ability <= 109: # ?블럭
            self.image.clip_draw(self.frame * 24, 1000 - 24, 24, 24, self.x, self.y, self.size[0], self.size[1])

        elif self.ability >= 110 and self.ability <= 120: # ?블럭 충돌
            self.image.clip_draw(self.frame * 24, 1000 - 24*2, 24, 24, self.x, self.y , self.size[0], self.size[1])


        elif self.ability == 2: # 일반 벽돌
            self.image.clip_draw(0, 1000 - 24 * 3, 24, 24, self.x, self.y, self.size[0], self.size[1])

        elif self.ability == 3: # 빛나는 벽돌(코인 벽돌)
            self.image.clip_draw(self.frame * 24, 1000 - 24 * 3, 24, 24, self.x, self.y , self.size[0], self.size[1])


        elif self.ability == 4: # 표정 벽돌 - 1
            self.image.clip_draw(0 * 24, 1000 - 24 * 4, 24, 24, self.x, self.y , self.size[0], self.size[1])

        elif self.ability == 5:  # 표정 벽돌 - 2
            self.image.clip_draw(1 * 24, 1000 - 24 * 4, 24, 24, self.x, self.y , self.size[0], self.size[1])


        elif self.ability == 98:
            # 철 블럭 (아무효과 X)
            self.image.clip_draw(9 * 24, 1000 - 24 * 2, 24, 24, self.x , self.y, self.size[0], self.size[1])

        elif self.ability == 99:
            # 아이템 블럭 사용 후 블럭 (아무효과 X)
            self.image.clip_draw(8 * 24, 1000 - 24 * 2, 24, 24, self.x , self.y, self.size[0], self.size[1])

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 16, self.y - 24, self.x + 16, self.y + 6

class object_item:
    image = None

    def __init__(self, x, y, ability=None):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.ability = ability
        self.dir = 1
        self.frame = 0
        self.JUMP = False
        self.g = 300
        self.ga = 9.8

        self.py = 0

        if ability >= 300:
            self.size = [32, 32]
        if ability == 303:
            self.starH = 0
        if object_item.image == None:
            object_item.image = load_image('object.png')
    def update(self):

        if self.ability >= 1000: # 생성
            if self.ability >= 1300:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
                if self.frame >= 10:
                    self.frame = 0
                    self.ability = self.ability - 1000


        else:
            self.py = self.move2y
            if self.ability == 303:
                if self.JUMP:
                    self.move2y += self.g * game_framework.frame_time
                    self.g -= self.ga
                    if self.g < 0:
                        self.JUMP = False

                else:
                    self.move2y -= self.g * game_framework.frame_time
                    self.g += self.ga
                    if self.g >= 900:
                        self.g = 900

            else:
                if self.JUMP:
                    self.move2y += self.g * game_framework.frame_time
                else:
                    self.move2y -= self.g * game_framework.frame_time


            if self.ability != 302:
                self.move2x += self.dir * 0.9 * 200 * game_framework.frame_time

        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

        self.check()


    def draw(self):
        if self.ability == 300:  # 일반 버섯
            self.image.clip_draw(0, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 301:  # 특수 버섯
            self.image.clip_draw(40 * 1, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 302:  # 꽃
            self.image.clip_draw(40 * 2, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 303:  # 별
            self.image.clip_draw(40 * 3, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 1300:  # 생성 일반 버섯
            self.image.clip_draw(40 * int(self.frame), 40, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 1301:
            self.image.clip_draw(40 * int(self.frame), 40 * 2, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 1302:
            self.image.clip_draw(40 * int(self.frame), 40 * 3, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 1303:
            self.image.clip_draw(40 * int(self.frame), 40 * 4, 40, 40, self.x, self.y, self.size[0], self.size[1])

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 14

    def check(self):
        if self.x < 0:
            self.dir = 1

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 2:  # 위서 아래로
                if self.ability == 303:
                    self.JUMP = True
                    self.g = 900
                else:
                    self.move2y = self.py
            elif contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1
            elif contact_aAndb(self, block) == 1:  # 아래서 위로
                self.JUMP = False

        for block in grounds:  # 블럭
            if contact_aAndb(self, block) == 2:  # 위서 아래로
                if self.ability == 303:
                    self.JUMP = True
                    self.g = 900
                else:
                    self.move2y = self.py
            elif contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1
            elif contact_aAndb(self, block) == 1:  # 아래서 위로
                self.JUMP = False

        if self.y <= -50:
            item.remove(self)
            game_world.remove_object(self)



class Ground:

    def __init__(self, leftx, lefty, rightx, righty, ability=999):
        self.rightx = rightx
        self.righty = righty
        self.leftx = leftx
        self.lefty = lefty
        self.x = (rightx + leftx) / 2
        self.y = (righty + lefty) / 2
        self.movex = 0
        self.movey = 0
        self.crex = self.x
        self.crey = self.y
        self.ability = ability
        self.size = [self.x - leftx, self.y - lefty]

    def update(self):
        self.x = self.crex + self.movex
        self.y = self.crey + self.movey

    def draw(self):
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.size[0], self.y - self.size[1], self.x + self.size[0], self.y + self.size[1]