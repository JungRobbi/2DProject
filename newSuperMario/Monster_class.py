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

class monster:
    def __init__(self, x, y, ability=None, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.ability = ability
        self.dir = dir
        self.frame = 0
        self.size = [48, 48]

        if monster.image == None:
            monster.image = load_image('Monster.png')

    def update(self):
        if self.ability == 5000:  # 굼바
            self.frame = (self.frame + 20 * game_framework.frame_time)
            if self.frame >= 10:
                self.frame = 0
                

    def draw(self):
        if self.ability == 5000:  # 일반 버섯
            self.image.clip_draw(0, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.ability == 304:
            return self.x - 6, self.y - 6, self.x + 6, self.y + 6
        return self.x - 16, self.y - 16, self.x + 16, self.y + 14

    def check(self):
        if self.x < 0:
            self.dir = 1

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 2:  # 위서 아래로
                if self.ability == 303:
                    self.JUMP = True
                    self.g = 900
                elif self.ability == 304:
                    self.JUMP = True
                    self.g = 300
                else:
                    self.move2y = self.py
            elif contact_aAndb(self, block) == 3:  # 좌우
                if self.ability == 304:
                    game_world.remove_object(self)

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
                elif self.ability == 304:
                    self.JUMP = True
                    self.g = 300
                else:
                    self.move2y = self.py
            elif contact_aAndb(self, block) == 3:  # 좌우
                if self.ability == 304:
                    game_world.remove_object(self)

                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1
            elif contact_aAndb(self, block) == 1:  # 아래서 위로
                self.JUMP = False

        if self.y <= -50:
            game_world.remove_object(self)



