from pico2d import *
import object_class

class monster:
    frame = 0
    fs = 0
    framedir = 0
    image = None

    def __init__(self, x, y, ability):
        self.x = x
        self.y = y
        self.movex = 0
        self.movey = 0
        self.crex = x
        self.crey = y
        self.ability = ability
        if monster.image == None:
            monster.image = load_image('Monster.png')

    def draw(self):
        if self.ability == 1000: # 굼바
            self.image.clip_draw(self.frame * 24, 1000 - 24, 24, 24, self.x, self.y, 48, 48)
            self.fs = self.fs + 1
            if self.fs == 18:
                self.fs = 0
                self.frame = (self.frame + 1) % 9

        self.x = self.crex + self.movex
        self.y = self.crey + self.movey