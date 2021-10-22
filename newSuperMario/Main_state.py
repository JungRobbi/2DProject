from pico2d import *
import game_framework
import Title_state


WINx = 1024
WINy = 600
moveWinx = 0
moveWiny = 0

Mario_image = None
object_image = None
map1 = None

mario = None
coin = []
Qblock = []
brick = []
skbrick = []

class hero:
    dir = 0
    herodir = 0
    status = 0
    xspeed = 0
    xMAX = 10.0
    xa = 0.02
    frame = 0
    fs = 0
    framedir = 0
    py = 0
    g = 6.0
    t = 0.0
    ga = 0.1
    size = [48, 60]

    def __init__(self,x, y):
        self.x = x
        self.y = y

    def update(self):
                    # 프레임
        if self.framedir == 0:
            if self.fs == 15:
                self.frame = self.frame + 1
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
                if self.frame >= 9:  # 정지 프레임
                    self.frame = 0
        else:
            if self.fs == 15:
                self.frame = self.frame - 1
            if self.frame <= 0:
                self.frame = 0
                self.framedir = 0
        self.fs = self.fs + 1
        if self.fs > 15:
            self.fs = 0
                # 이동
        self.move()

    def draw(self):
        if self.status != 0: # 점프 등의 특수 상태
           if self.dir == 0:  # 정지
               if self.herodir == 1:
                   Mario_image.clip_draw(self.frame * 32, 960 - 2 * 40, 32, 40, self.x, self.y, self.size[0],self.size[1] )
               else:
                   Mario_image.clip_composite_draw(self.frame * 32, 960 - 2 * 40, 32, 40, 0, 'h', self.x, self.y, self.size[0],self.size[1])
           if self.dir == 1:
               Mario_image.clip_draw(self.frame * 32, 960 - 2 * 40, 32, 40, self.x, self.y, self.size[0],self.size[1])
           elif self.dir == -1:
               Mario_image.clip_composite_draw(self.frame * 32, 960 - 2 * 40, 32, 40, 0, 'h', self.x, self.y, self.size[0],self.size[1])
        else: # 기본 이동 스프라이트
           if self.dir == 0:  # 정지
               if self.herodir == 1:
                   Mario_image.clip_draw(self.frame * 32, 960 - 40, 32, 40, self.x, self.y, self.size[0],self.size[1])
               else:
                   Mario_image.clip_composite_draw(self.frame * 32, 960 - 40, 32, 40, 0, 'h', self.x, self.y, self.size[0],self.size[1])
           elif self.dir == 1:  # 오른쪽 걸음
               Mario_image.clip_draw(self.frame * 32, 960, 32, 40, self.x, self.y, self.size[0],self.size[1])
           elif self.dir == -1:  # 왼쪽 걸음
               Mario_image.clip_composite_draw(self.frame * 32, 960, 32, 40, 0, 'h', self.x, self.y, self.size[0],self.size[1])

    def move(self):
        if self.status == 1: # 상승
            self.y = -(self.ga/2) * (self.t ** 2) + self.g * self.t + self.py
            self.t += 1
            if (self.ga/2) * (self.t ** 2) > self.g * self.t:
                self.status = -1
        elif self.status == -1: # 하강
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

    def update(self):
      pass


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





class monster:
    frame = 0
    fs = 0
    framedir = 0

    def __init__(self, x, y, tribe):
        self.x = x
        self.y = y
        self.tribe = tribe

    def draw(self):

        pass

def enter(): # 생성
    global Mario_image, object_image, map1
    ground1 = 65

    mapcreate(1, ground1)

    Mario_image = load_image('MarioMove.png')
    object_image = load_image('object.png')
    map1 = load_image('1-1.png')
def exit(): # 종료/제거
    global mario, coin, Qblock, brick, skbrick
    del (mario)
    del (coin)
    del (Qblock)
    del (brick)
    del (skbrick)

def handle_events():
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.frame = 0
                mario.framedir = 0
                mario.xspeed = 0
            elif event.key == SDLK_LEFT:
                mario.dir -= 1
                mario.frame = 0
                mario.framedir = 0
                mario.xspeed = 0
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
    delay(0.001)

def draw():
    clear_canvas()
    map1.clip_draw(0, 0, 4222, 624, 2110 * 2.5 + moveWinx, 120 * 2.5 + moveWiny, 4224 * 2.5, 624 * 2.5)
    mario.draw()
    for c in coin:
        c.draw()
    for b in Qblock:
        b.draw()
    for b in brick:
        b.draw()
    for b in skbrick:
        b.draw()
    update_canvas()

def pause():
    pass


def resume():
    pass


def mapcreate(map , ground1):
    global mario, coin, Qblock, brick, skbrick

    if map == 1:
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


