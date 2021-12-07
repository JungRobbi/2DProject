from pico2d import *
import game_framework
import game_world

from Mario_class import *
from Map import map
from object_variable import *
import object_class
import Monster_class

name = "MainState"

map1_1 = None
stage = None
Num_image_black = None
Num_image_white = None
Timer = None
mario = None

def get_Timer():
    return Timer

def get_mario():
    global mario
    return mario

def enter():
    global map1_1
    global SET_BLOCK
    global CHANGE_TIME; global CHANGE_image; global CHANGE_INOUT
    global Num_image_black, Num_image_white
    global Timer
    global mario

    f = open("Stage.txt", 'r')
    line = f.readline()
    data = int(line)
    f.close()

    mario = hero(40, 300, data)
    if data == 2:
        game_framework.change_state(end_state)
    else:

        map1_1 = map(data)

        game_world.add_object(map1_1, 0)
        mapcreate(map1_1)
        SET_BLOCK = grounds[0]

        CHANGE_TIME = 1.0
        CHANGE_image = load_image('change_effect_1.png')
        CHANGE_INOUT = 'IN'

        Num_image_black = load_image('font_Black.png')
        Num_image_white = load_image('font_White.png')
        Timer = 300

def exit():
    global grounds, coin, Qblock, brick, skbrick, Steelblock, item, monsters, mario
    global SET_BLOCK,CHANGE_TIME,CHANGE_image,CHANGE_INOUT, BOOL_CLEAR

    grounds.clear()
    coin.clear()
    Qblock.clear()
    brick.clear()
    skbrick.clear()
    Steelblock.clear()
    item.clear()
    monsters.clear()

    game_world.clear()

    SET_BLOCK = None
    CHANGE_TIME = None
    CHANGE_image = None
    CHANGE_INOUT = None

    BOOL_CLEAR = False

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mario.handle_event(event)


def update():
    global CHANGE_TIME;  global CHANGE_INOUT, Timer, map1_1
    if CHANGE_TIME >= 0:
        CHANGE_TIME -= game_framework.frame_time*2

    else:
        if Timer > 0:
            Timer -= game_framework.frame_time
        elif Timer < 0:
            mario.add_event(DIE)
            mario.g = 1100.0
            mario.JUMP = True
            mario.frame = 0
            Timer = 0
        mapmove(map1_1, mario)
        for game_object in game_world.all_objects():
            game_object.update()

        if mario.IVtimer <= 0:
            mario.check()
        else:
            mario.IVtimer -= game_framework.frame_time

        if not map1_1.moveWinx == map1_1.mapmax and mario.cur_state == ClearState:
            mario.cur_state = IdleState





def draw():
    global CHANGE_TIME; global CHANGE_image, mario, Num_image_black, Timer

    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    if CHANGE_TIME >= 0:
        if CHANGE_INOUT == 'IN':
            CHANGE_image.clip_draw(512 - int(512 * CHANGE_TIME),300 - int(300 * CHANGE_TIME),2 * int(512 * CHANGE_TIME), 2 * int(300 * CHANGE_TIME), 512, 300, 1024, 600)
            # in > out
        else:
            CHANGE_image.clip_draw(0 + int(512 * CHANGE_TIME),0 + int(300 * CHANGE_TIME),1024 - 2 * int(512 * CHANGE_TIME), 600 - 2 * int(300 * CHANGE_TIME), 512, 300, 1024, 600)
            # out > in

    if int(mario.score / 100) == 9:Num_image_black.clip_composite_draw(24, 286 - 120, 64, 64, 0, '', 32, 600 - 32, 32, 32)
    else:Num_image_black.clip_composite_draw(24 + int(mario.score / 100) * 110, 286, 64, 64, 0, '', 32, 600 - 32, 32, 32)
    if int(mario.score % 100 / 10) == 9:Num_image_black.clip_composite_draw(24, 286 - 120, 64, 64, 0, '', 32 * 2, 600 - 32, 32, 32)
    else:Num_image_black.clip_composite_draw(24 + int(mario.score % 100 / 10) * 110, 286, 64, 64, 0, '', 32 * 2, 600 - 32, 32, 32)
    if int(mario.score % 10) == 9:Num_image_black.clip_composite_draw(24, 286 - 120, 64, 64, 0, '', 32 * 3, 600 - 32, 32, 32)
    else:Num_image_black.clip_composite_draw(24 + int(mario.score % 10) * 110, 286, 64, 64, 0, '', 32 * 3, 600 - 32, 32, 32)


    if int(Timer / 100) == 9:Num_image_white.clip_composite_draw(24, 286 - 120, 64, 64, 0, '', 32 + 900, 600 - 32, 32, 32)
    else:Num_image_white.clip_composite_draw(24 + int(Timer / 100) * 110, 286, 64, 64, 0, '', 32 + 900, 600 - 32, 32, 32)
    if int(Timer % 100 / 10) == 9:Num_image_white.clip_composite_draw(24, 286 - 120, 64, 64, 0, '', 32 * 2 + 900, 600 - 32, 32, 32)
    else:Num_image_white.clip_composite_draw(24 + int(Timer % 100 / 10) * 110, 286, 64, 64, 0, '', 32 * 2 + 900, 600 - 32, 32, 32)
    if int(Timer % 10) == 9:Num_image_white.clip_composite_draw(24, 286 - 120, 64, 64, 0, '', 32 * 3 + 900, 600 - 32, 32, 32)
    else:Num_image_white.clip_composite_draw(24 + int(Timer % 10) * 110, 286, 64, 64, 0, '', 32 * 3 + 900, 600 - 32, 32, 32)



    update_canvas()


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



def mapmove(map, mario):
    WINx = 1024
    WINy = 600

    map.mapmax = -(4222 * 2 + WINx - 15)

    if map.moveWinx < map.mapmax:
        map.moveWinx = map.mapmax
    if map.moveWinx > 0:
        map.moveWinx = 0

    if map.moveWinx < 0 and mario.x < WINx * 3 / 5 and mario.velocity == -1:
        if mario.x + mario.xMAX >= WINx * 3 / 5:
            map.moveWinx += mario.xspeed * game_framework.frame_time
        else:
            map.moveWinx += mario.xspeed * 2 * game_framework.frame_time
        mario.x += mario.xspeed * 1.3 * game_framework.frame_time
        if mario.x > WINx * 3 / 5:
            mario.x = WINx * 3 / 5

    if map.moveWinx > map.mapmax and mario.x > WINx * 2 / 5 and mario.velocity == 1:
        if mario.x - mario.xMAX <= WINx * 2 / 5:
            map.moveWinx -= mario.xspeed * game_framework.frame_time
        else:
            map.moveWinx -= mario.xspeed * 2 * game_framework.frame_time
        mario.x -= mario.xspeed * 1.3 * game_framework.frame_time
        if mario.x < WINx * 2 / 5:
            mario.x = WINx * 2 / 5

    if map.moveWinx < 0 and mario.x < WINx * 3 / 5 and mario.velocity == 0 and mario.dir == -1:
        if mario.x + mario.xMAX >= WINx * 3 / 5:
            map.moveWinx += mario.xspeed * game_framework.frame_time
        else:
            map.moveWinx += mario.xspeed * 2 * game_framework.frame_time
        mario.x += mario.xspeed * 1.3 * game_framework.frame_time
        if mario.x > WINx * 3 / 5:
            mario.x = WINx * 3 / 5

    if map.moveWinx > map.mapmax and mario.x > WINx * 2 / 5 and mario.velocity == 0 and mario.dir == 1:
        if mario.x - mario.xMAX <= WINx * 2 / 5:
            map.moveWinx -= mario.xspeed * game_framework.frame_time
        else:
            map.moveWinx -= mario.xspeed * 2 * game_framework.frame_time
        mario.x -= mario.xspeed * 1.3 * game_framework.frame_time
        if mario.x < WINx * 2 / 5:
            mario.x = WINx * 2 / 5

    for game_object in game_world.all_objects():
        game_object.movex = map.moveWinx
        game_object.movey = map.moveWiny


        # 완료

def mapcreate(map):
    if map.stage == 0:

        ground1 = 65

        #  몬스터
        # monsters.append(Monster_class.goomba(350 * 2.5, (14 + 8) * 2.5))
        # monsters.append(Monster_class.goomba(700 * 2.5, (14 + 8) * 2.5))
        # monsters.append(Monster_class.goomba(800 * 2.5, (14 + 8) * 2.5))
        # monsters.append(Monster_class.goomba(900 * 2.5, (14 + 8) * 2.5))
        #
        # monsters.append(Monster_class.goomba(1900 * 2.5, (14 + 8) * 2.5))
        # monsters.append(Monster_class.goomba(2200 * 2.5, (14 + 8) * 2.5))
        #
        # monsters.append(Monster_class.boo(800 * 2.5, 100 * 2.5))
        # monsters.append(Monster_class.boo(1180 * 2.5, 100 * 2.5))
        #
        # monsters.append(Monster_class.Hammer_bros(1421 * 2.5, (14 + 12) * 2.5, -1, -221 * 2.5, 221 * 2.5))

        monsters.append(Monster_class.plant(990 * 2.5, (46 + 14) * 2.5))
        monsters.append(Monster_class.plant(2318 * 2.5, (46 + 14) * 2.5))

        grounds.append(object_class.Ground(0, 0, 2914, 35))
        grounds.append(object_class.Ground(434 * 2.5, 0, 514 * 2.5, 30 * 2.5))
        grounds.append(object_class.Ground(512 * 2.5, 0, (514+92) * 2.5, 62 * 2.5))
        grounds.append(object_class.Ground(2914 + 36 * 2.5, 0, 2914 + (36+444) * 2.5, 14 * 2.5))
        grounds.append(object_class.Ground(2914 + (36 * 2 + 444) * 2.5, 0, 2914 + (36*2 + 444 + 924) * 2.5, 14 * 2.5))
        grounds.append(object_class.Ground(2914 + (36*3 + 1366) * 2.5, 0, 2914 + (36 * 3 + 1842) * 2.5, 14 * 2.5))

        # 큰 언덕
        grounds.append(object_class.Ground(2914 + (36 * 3 + 1366 + 112) * 2.5, 0, 2914 + (36 * 3 + 1366 + 236) * 2.5, 30 * 2.5))
        grounds.append(object_class.Ground(2914 + (36 * 3 + 1366 + 288) * 2.5, 0, 2914 + (36 * 3 + 1366 + 288 + 188) * 2.5, 30 * 2.5))
        grounds.append(object_class.Ground(2914 + (36 * 3 + 1366 + 176) * 2.5, 0, 2914 + (36 * 3 + 1366 + 236) * 2.5, 62 * 2.5))
        grounds.append(object_class.Ground(2914 + (36 * 3 + 1366 + 288) * 2.5, 0, 2914 + (36 * 3 + 1366 + 396) * 2.5, 62 * 2.5))

        grounds.append(object_class.Ground(2914 + (36 * 3 + 1878) * 2.5, 0, 2914 + (36 * 3 + 1878 + 364) * 2.5, 14 * 2.5))
        grounds.append(object_class.Ground(2914 + (36 * 3 + 2294) * 2.5, 0, 2914 + (36 * 3 + 2294 + 52 + 652) * 2.5, 14 * 2.5))

        grounds.append(object_class.Ground(2914 - (191) * 2.5, 0, 2914 - (159) * 2.5, 46 * 2.5, 900))
        grounds.append(object_class.Ground(2914 - (191 - 784) * 2.5, 0, 2914 - (159 - 784) * 2.5, 62 * 2.5, 900))
        grounds.append(object_class.Ground(2914 - (191 - 784 - 544) * 2.5, 0, 2914 - (159 - 784 - 544) * 2.5, 46 * 2.5, 900))
        grounds.append(object_class.Ground(2914 - (191 - 784 - 544 - 944) * 2.5, 0, 2914 - (159 - 784 - 544 - 944) * 2.5, 46 * 2.5,900))

        grounds.append(object_class.Ground(3980 * 2.5, 14 * 2.5, (3980 + 4) * 2.5, 174 * 2.5,950))



        # Qblock.append(object_class.object(48 * 3, ground1 + 60 * 2, 101))
        # Qblock.append(object_class.object(48 * 4, ground1 + 60 * 2, 102))
        # Qblock.append(object_class.object(48 * 5, ground1 + 60 * 2, 103))
        # Qblock.append(object_class.object(48 * 6, ground1 + 60 * 2, 104))

        Qblock.append(object_class.object(48 * 12, ground1 + 60 * 2, 101))
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
        Qblock.append(object_class.object(48 * 35 + 32, ground1 + 60 * 5, 103))

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

        brick.append(object_class.object(48 * 108, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 108 + 32, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 108 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object_class.object(48 * 108 + 32 * 3, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 4, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 5, ground1 + 60 * 2, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 6, ground1 + 60 * 2, 100))
        brick.append(object_class.object(48 * 108 + 32 * 7, ground1 + 60 * 2, 2))
        brick.append(object_class.object(48 * 108 + 32 * 8, ground1 + 60 * 2, 2))

        Qblock.append(object_class.object(48 * 108 + 32 * 3, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 4, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object_class.object(48 * 108 + 32 * 5, ground1 + 60 * 4 + 32, 102))

        skbrick.append(object_class.object(48 * 125, ground1 + 60 * 2, 4))
        skbrick.append(object_class.object(48 * 127, ground1 + 60 * 2, 4))
        skbrick.append(object_class.object(48 * 129, ground1 + 60 * 2, 4))

        coin.append(object_class.object(48 * 136, ground1 + 60 * 2, 0))
        coin.append(object_class.object(48 * 136 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 136 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object_class.object(48 * 136 + 32 * 3, ground1 + 60 * 2, 0))

        Qblock.append(object_class.object(48 * 142, ground1 + 60 * 2, 104))

        brick.append(object_class.object(48 * 151 - 37, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 - 5, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 + 27, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 + 32 * 2 - 5, ground1 + 60 + 20, 2))

        Qblock.append(object_class.object(48 * 156, ground1 + 60 * 4, 103))

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
            for i in range(0, k):
                Steelblock.append(object_class.object(48 * 200 - 32 * i, ground1 + 32 * 8 - 32 * k - 10, 98))



    elif map.stage == 1:

        grounds.append(object_class.Ground(0 * 2.5, 42 * 2.5, 94 * 2.5, 58 * 2.5))
        grounds.append(object_class.Ground(158 * 2.5, 26 * 2.5, 286 * 2.5, 42 * 2.5))
        grounds.append(object_class.Ground((336 - 2) * 2.5, (12 - 2) * 2.5, (560 - 2) * 2.5, (28 - 2) * 2.5))
        grounds.append(object_class.Ground((621 - 2) * 2.5, (12 - 2) * 2.5, (720 - 2) * 2.5, (28 - 2) * 2.5))
        grounds.append(object_class.Ground((750 - 2) * 2.5, (12 - 2) * 2.5, (929 - 2) * 2.5, (28 - 2) * 2.5))

        grounds.append(object_class.Ground((956 - 2) * 2.5, (36 - 2) * 2.5, (1088 - 2) * 2.5, (60 - 2) * 2.5))
        grounds.append(object_class.Ground((1120 - 2) * 2.5, (12 - 2) * 2.5, (1343 - 2) * 2.5, (28 - 2) * 2.5))

        grounds.append(object_class.Ground((1356 - 2) * 2.5, (51 - 2) * 2.5, (1395 - 2) * 2.5, (76 - 2) * 2.5))
        grounds.append(object_class.Ground((1436 - 2) * 2.5, (51 - 2) * 2.5, (1572 - 2) * 2.5, (76 - 2) * 2.5))

        grounds.append(object_class.Ground((1612 - 2) * 2.5, (4 - 2) * 2.5, (1684 - 2) * 2.5, (28 - 2) * 2.5))
        grounds.append(object_class.Ground((1728 - 2) * 2.5, (12 - 2) * 2.5, (1876 - 2) * 2.5, (28 - 2) * 2.5))

        grounds.append(object_class.Ground((1920 - 2) * 2.5, (28 - 2) * 2.5, (1988 ) * 2.5, (44 - 2) * 2.5))

        grounds.append(object_class.Ground((1984 - 2) * 2.5, (76 - 2) * 2.5, (2032 ) * 2.5, (92 - 2) * 2.5))
        grounds.append(object_class.Ground((1897 - 2) * 2.5, (108 - 2) * 2.5, (1958 ) * 2.5, (122 - 2) * 2.5))
        grounds.append(object_class.Ground((1760 - 2) * 2.5, (124 - 2) * 2.5, (1808) * 2.5, (140 - 2) * 2.5))

        grounds.append(object_class.Ground((2080 - 2) * 2.5, (44 - 2) * 2.5, (2144) * 2.5, (60 - 2) * 2.5))

        grounds.append(object_class.Ground((2176 - 2) * 2.5, (52 - 2) * 2.5, (2271 ) * 2.5, (76 - 2) * 2.5))

        grounds.append(object_class.Ground((2336 - 2) * 2.5, (36 - 2) * 2.5, (2400 ) * 2.5, (60 - 2) * 2.5))

        grounds.append(object_class.Ground((2448 - 2) * 2.5, (20 - 2) * 2.5, (2512 ) * 2.5, (44 - 2) * 2.5))
        grounds.append(object_class.Ground((2576 - 2) * 2.5, (20 - 2) * 2.5, (2640 ) * 2.5, (44 - 2) * 2.5))

        grounds.append(object_class.Ground((2720 - 2) * 2.5, (12 - 2) * 2.5, (2864 ) * 2.5, (28 - 2) * 2.5))
        grounds.append(object_class.Ground((2864 - 2) * 2.5, (60 - 2) * 2.5, (2912 ) * 2.5, (76 - 2) * 2.5))
        grounds.append(object_class.Ground((2784 - 2) * 2.5, (108 - 2) * 2.5, (2832 ) * 2.5, (124 - 2) * 2.5))

        grounds.append(object_class.Ground((2976 - 2) * 2.5, (35 - 2) * 2.5, (3008 ) * 2.5, (59 - 2) * 2.5))
        grounds.append(object_class.Ground((3056 - 2) * 2.5, (42 - 2) * 2.5, (3088 ) * 2.5, (66 - 2) * 2.5))

        grounds.append(object_class.Ground((3120 - 2) * 2.5, (12 - 2) * 2.5, (3136 ) * 2.5, (28 - 2) * 2.5))
        grounds.append(object_class.Ground((3152 - 2) * 2.5, (83 - 2) * 2.5, (3184 ) * 2.5, (107 - 2) * 2.5))
        grounds.append(object_class.Ground((3200 - 2) * 2.5, (12 - 2) * 2.5, (3216 ) * 2.5, (28 - 2) * 2.5))
        grounds.append(object_class.Ground((3264 - 2) * 2.5, (2 - 2) * 2.5, (3296 ) * 2.5, (12 - 2) * 2.5))

        grounds.append(object_class.Ground((3360 - 2) * 2.5, (12 - 2) * 2.5, (3456 ) * 2.5, (36 - 2) * 2.5))

        grounds.append(object_class.Ground((3504 - 2) * 2.5, (26 - 2) * 2.5, (3696 ) * 2.5, (42 - 2) * 2.5))
        grounds.append(object_class.Ground((3616 - 2) * 2.5, (100 - 2) * 2.5, (3648 ) * 2.5, (124 - 2) * 2.5))

        grounds.append(object_class.Ground((3744 - 2) * 2.5, (84 - 2) * 2.5, (3872 ) * 2.5, (108 - 2) * 2.5))


    game_world.add_object(mario, 1)
    for i in grounds + coin + Qblock + brick + skbrick + Steelblock + item + monsters:
        game_world.add_object(i, 1)



