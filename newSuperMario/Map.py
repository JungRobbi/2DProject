from pico2d import *

from Mario_class import hero

class map:
    def __init__(self, stage):
        if stage == 0:
            self.image = load_image('1-1.png')

        self.stage = stage
        self.x = 0
        self.y = 0
        self.moveWinx = 0
        self.moveWiny = 0
        self.mapmax = 0


    def update(self):
        pass

    def draw(self):
        if self.stage == 0:
            self.image.clip_draw(0, 0, 4224, 624, 2110 * 2.5 + self.moveWinx, 120 * 2.5 + self.moveWiny, 4224 * 2.5, 624 * 2.5)
