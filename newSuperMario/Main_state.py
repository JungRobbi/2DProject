from pico2d import *
import game_framework
import Title_state

import Mario_class
import Monster_class
import object_class


WINx = 1024
WINy = 600
moveWinx = 0
moveWiny = 0
stage = 1

object_image = None
Monster_image = None
map1 = None
map2 = None

#hero
mario = None
#ground
grounds = []
#block
coin = []
Qblock = []
brick = []
skbrick = []
Steelblock = []

#item
item = []

#monster
monsters = []



def enter(): # 생성
    global Mario_image, object_image, Monster_image, map1, map2, stage

    stage = 1
    mapcreate(stage)

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
        elif event.type == SDL_KEYDOWN and mario.status < 99:
            if event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.framedir = 0
                mario.xspeed = 0
                if mario.herodir == 1:
                    mario.frame = 4
                else:
                    mario.frame = 0

                mario.herodir = 1
            elif event.key == SDLK_LEFT:
                mario.dir -= 1
                mario.framedir = 0
                mario.xspeed = 0
                mario.frame = 0
                if mario.herodir == -1:
                    mario.frame = 4
                else:
                    mario.frame = 0

                mario.herodir = -1
            elif event.key == SDLK_UP and mario.status == 0:
                mario.py = mario.y
                mario.status = 1
                mario.sit = 0
                mario.frame = 0
                mario.framedir = 0
            elif event.key == SDLK_DOWN:
                mario.sit = 1
                mario.frame = 0
                mario.xspeed = 0
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(Title_state)
        elif event.type == SDL_KEYUP and mario.status != 99:
            if event.key == SDLK_RIGHT:
                mario.dir -= 1
            elif event.key == SDLK_LEFT:
                mario.dir += 1
            if event.key == SDLK_DOWN:
                mario.sit = 0

def update():
    mapmove()

    mario.update()
    for i in grounds + Qblock + item:
        mario.contact_check(i)

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
    for m in monsters:
        m.draw()

    mario.draw()
    update_canvas()


def pause():
    pass

def resume():
    pass


def mapcreate(map):
    global mario, coin, Qblock, brick, skbrick, Steelblock
    global monsters

    if map == 1:
        ground1 = 65
        mario = Mario_class.hero(50, 75)


        grounds.append(object_class.Ground(0, 0, 1168 * 2, 40))

        # Qblock.append(object(48 * 8, ground1 + 32 * 2, 100))
        # Qblock.append(object(48 * 8, ground1 + 32 * 1, 100))
        Qblock.append(object_class.object(48 * 8, ground1, 100))

        Qblock.append(object_class.object(48 * 12, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 15, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 15 + 32, ground1 + 60 * 2, 100))

        coin.append(object_class.object(48 * 22, ground1 + 60 * 1, 0))
        coin.append(object_class.object(48 * 22 + 32, ground1 + 60 * 1 + 32, 0))
        coin.append(object_class.object(48 * 22 + 32 * 2, ground1 + 60 * 1 + 32, 0))

        coin.append(object_class.object(48 * 26, ground1 + 60 * 2, 0))
        coin.append(object_class.object(48 * 26 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 26 + 32 * 2, ground1 + 60 * 2 + 32, 0))

        skbrick.append(object_class.object(48 * 29, ground1 + 60 * 4, 3))

        brick.append(object_class.object(48 * 35, ground1 + 60 * 2, 2))
        skbrick.append(object_class.object(48 * 35 + 32, ground1 + 60 * 2, 3))
        brick.append(object_class.object(48 * 35 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object_class.object(48 * 35 + 32, ground1 + 60 * 5, 100))

        coin.append(object_class.object(48 * 42, ground1 + 60 * 2, 0))
        coin.append(object_class.object(48 * 42 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 42 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 42 + 32 * 3, ground1 + 60 * 2, 0))

        coin.append(object_class.object(48 * 61, ground1 + 60 * 2, 0))
        coin.append(object_class.object(48 * 61 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 61 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 61 + 32 * 3, ground1 + 60 * 2, 0))

        brick.append(object_class.object(48 * 75, ground1 + 60 * 2, 2))
        Qblock.append(object_class.object(48 * 75 + 32, ground1 + 60 * 2, 100))
        brick.append(object_class.object(48 * 75 + 32 * 2, ground1 + 60 * 2, 2))

        Qblock.append(object_class.object(48 * 81, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 81 + 32, ground1 + 60 * 2, 100))

        coin.append(object_class.object(48 * 86, ground1 + 60 * 2, 0))
        coin.append(object_class.object(48 * 86 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 86 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 86 + 32 * 3, ground1 + 60 * 2, 0))

        coin.append(object_class.object(48 * 94, ground1 + 60 * 4, 0))
        coin.append(object_class.object(48 * 94 + 32, ground1 + 60 * 4 + 32, 0))
        coin.append(object_class.object(48 * 94 + 32 * 2, ground1 + 60 * 4 + 32, 0))
        Qblock.append(object_class.object(48 * 94 + 32 * 2, ground1 + 60 * 3, 100))
        Qblock.append(object_class.object(48 * 94 + 32 * 3, ground1 + 60 * 3, 101))
        Qblock.append(object_class.object(48 * 94 + 32 * 4, ground1 + 60 * 3, 100))
        brick.append(object_class.object(48 * 94 + 32 * 5, ground1 + 60 * 3, 2))
        brick.append(object_class.object(48 * 94 + 32 * 6, ground1 + 60 * 3, 2))

        brick.append(object_class.object(48 * 108 , ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 108 + 32, ground1 + 60 * 2, 2))
        skbrick.append(object_class.object(48 * 108 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object_class.object(48 * 108 + 32 * 3, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 4, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 5, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 6, ground1 + 60 * 2, 100))
        brick.append(object_class.object(48 * 108 + 32 * 7, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 108 + 32 * 8, ground1 + 60 * 2, 2))

        Qblock.append(object_class.object(48 * 108 + 32 * 3, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 4, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 5, ground1 + 60 * 4 + 32, 100))

        skbrick.append(object_class.object(48 * 125, ground1 + 60 * 2, 2))
        skbrick.append(object_class.object(48 * 127, ground1 + 60 * 2, 2))
        skbrick.append(object_class.object(48 * 129, ground1 + 60 * 2, 2))

        coin.append(object_class.object(48 * 136, ground1 + 60 * 2, 0))
        coin.append(object_class.object(48 * 136 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 136 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 136 + 32 * 3, ground1 + 60 * 2, 0))

        Qblock.append(object_class.object(48 * 142, ground1 + 60 * 2, 102))

        brick.append(object_class.object(48 * 151 - 37, ground1 + 60 + 20 , 2))
        brick.append(object_class.object(48 * 151 - 5, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 + 27, ground1 + 60 + 20 , 2))
        brick.append(object_class.object(48 * 151 + 32 * 2 - 5, ground1 + 60 + 20 , 2))

        Qblock.append(object_class.object(48 * 156, ground1 + 60 * 4, 100))

        coin.append(object_class.object(48 * 162 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 162 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 162 + 32 * 3, ground1 + 60 * 2, 0))

        brick.append(object_class.object(48 * 175, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 175 + 32, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 175 + 32 * 2, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 175 + 32 * 3, ground1 + 60 * 2, 2))

        brick.append(object_class.object(48 * 189, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 189 + 32, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 189 + 32 * 2, ground1 + 60 * 2, 2))


        for k in range(8, 1, -1):
            for i in range(0,k):
                Steelblock.append(object_class.object(48 * 200 - 32 * i, ground1 + 32 * 8 - 32 * k - 10, 98))


        monsters.append(Monster_class.monster(48 * 10, ground1 - 10, 1000))
        item.append(object_class.object_item(48 * 3, ground1 - 15, 300))
        item.append(object_class.object_item(48 * 4, ground1 - 15, 301))
        item.append(object_class.object_item(48 * 5, ground1 - 15, 302))
        item.append(object_class.object_item(48 * 6, ground1 - 15, 303))

    elif map == 2:
        mario = Mario_class.hero(50, 60)


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

        # 완료


