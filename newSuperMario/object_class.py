from pico2d import *

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
        elif self.ability >= 100 and self.ability <= 110:  # ?블럭
            self.fs = self.fs + 1
            if self.fs == 30:
                self.fs = 0
                self.frame = (self.frame + 1) % 4
        elif self.ability >= 111 and self.ability <= 120:  # ?블럭 충돌
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
            return self.x - 16, self.y - 24, self.x + 16, self.y + 10

class object_item:
    image = None

    def __init__(self, x, y, ability=None):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.crex = x
        self.crey = y
        self.ability = ability
        self.dir = 1
        if self.ability == 303:
            self.status = 1
            self.ga = 0.1
            self.g = 6.0
            self.t = 0
            self.py = self.y

        if ability >= 300:
            self.size = [32, 32]
        if object_item.image == None:
            object_item.image = load_image('object.png')
    def update(self):
        if self.ability == 303:
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

        if self.ability != 302:
            self.move2x += self.dir * 0.9

        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey

    def draw(self):
        if self.ability == 300:  # 일반 버섯
            self.image.clip_draw(0, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 301:  # 특수 버섯
            self.image.clip_draw(40 * 1, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 302:  # 꽃
            self.image.clip_draw(40 * 2, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])
        elif self.ability == 303:  # 별
            self.image.clip_draw(40 * 3, 0, 40, 40, self.x, self.y, self.size[0], self.size[1])

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 14

class Ground:

    def __init__(self, leftx, lefty, rightx, righty):
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
        self.ability = 999
        self.size = [self.x - leftx, self.y - lefty]

    def update(self):
        self.x = self.crex + self.movex
        self.y = self.crey + self.movey

    def draw(self):
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.size[0], self.y - self.size[1], self.x + self.size[0], self.y + self.size[1]
