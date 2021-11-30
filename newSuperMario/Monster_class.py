from pico2d import *
import game_framework
from object_variable import *
import game_world

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

    if top_a - (a.g + 5.0) * game_framework.frame_time < bottom_b: return 1 # 아래에서 위로
    if bottom_a + (a.g + 5.0) * game_framework.frame_time > top_b: return 2 # 위에서 아래로

    return 3 # 좌,우

class goomba:
    image = None
    def __init__(self, x, y, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.dir = dir
        self.frame = 0
        self.size = [40, 40]
        self.g = 0
        if goomba.image == None:
            goomba.image = load_image('Monster.png')

    def update(self):
        self.frame = (self.frame + 10 * game_framework.frame_time)
        if self.frame >= 9:
            self.frame = 0
        self.move2x += self.dir * 0.9 * 100 * game_framework.frame_time
        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

        self.check()


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 24, 1000 - 24, 24, 24, self.x, self.y, self.size[0], self.size[1])
        else:
            self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 24, 24, 24, 0, 'h', self.x, self.y,
                                           self.size[0], self.size[1])
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 13, self.y - 12, self.x + 13, self.y + 12

    def check(self):
        if self.x < 0:
            self.dir = 1

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1

        for block in grounds:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1


class boo:
    image = None
    def __init__(self, x, y, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.dir = dir
        self.frame = 0
        self.size = [40, 40]
        self.g = 0
        if boo.image == None:
            boo.image = load_image('Monster.png')

    def update(self):
        self.frame = (self.frame + 10 * game_framework.frame_time)
        if self.frame >= 3:
            self.frame = 0
        self.move2x += self.dir * 0.9 * 100 * game_framework.frame_time
        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

        self.check()


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 24, 1000 - 2 * 24, 24, 24, self.x, self.y, self.size[0], self.size[1])
        else:
            self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 2 * 24, 24, 24, 0, 'h', self.x, self.y,
                                           self.size[0], self.size[1])
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 15, self.y + 15

    def check(self):
        if self.x < 0:
            self.dir = 1

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1

        for block in grounds:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1


class Hammer_bros:
    image = None
    def __init__(self, x, y, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.dir = dir
        self.frame = 0
        self.size = [40, 67]
        self.g = 0
        if Hammer_bros.image == None:
            Hammer_bros.image = load_image('Monster.png')

    def update(self):
        self.frame = (self.frame + 10 * game_framework.frame_time)
        if self.frame >= 25:
            self.frame = 0
        self.move2x += self.dir * 0.9 * 100 * game_framework.frame_time
        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

        self.check()


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 24, 1000 - 2 * 24 - 40, 24, 40, self.x, self.y, self.size[0], self.size[1])
        else:
            self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 2 * 24 - 40, 24, 40, 0, 'h', self.x, self.y,
                                           self.size[0], self.size[1])
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 15, self.y + 15

    def check(self):
        if self.x < 0:
            self.dir = 1

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1

        for block in grounds:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1



