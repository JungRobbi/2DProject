from pico2d import *
import game_framework
import game_world

from Mario_class import hero
from Map import map
import object_class

name = "MainState"

mario = None
map1_1 = None
def enter():
    global mario
    global map1_1
    mario = hero(40, 60)
    stage = 0
    map1_1 = map(stage)
    game_world.add_object(map1_1, 0)
    mapcreate(stage)


    game_world.add_object(mario, 1)


def exit():
    game_world.clear()

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
    mapmove(map1_1, mario)
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.001)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def contact_aAndb(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mapmove(map, mario):
    WINx = 1024
    WINy = 600
    if map.stage == 0:
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
            mario.x += mario.xspeed * 2 * game_framework.frame_time
            if mario.x > WINx * 3 / 5:
                mario.x = WINx * 3 / 5

        if map.moveWinx > map.mapmax and mario.x > WINx * 2 / 5 and mario.velocity == 1:
            if mario.x - mario.xMAX <= WINx * 2 / 5:
                map.moveWinx -= mario.xspeed * game_framework.frame_time
            else:
                map.moveWinx -= mario.xspeed * 2 * game_framework.frame_time
            mario.x -= mario.xspeed * 2 * game_framework.frame_time
            if mario.x < WINx * 2 / 5:
                mario.x = WINx * 2 / 5

    for game_object in game_world.all_objects():
        game_object.movex = map.moveWinx
        game_object.movey = map.moveWiny

        # 완료

def mapcreate(stage):
    if stage == 0:
        # ground
        grounds = []
        # block
        coin = []
        Qblock = []
        brick = []
        skbrick = []
        Steelblock = []

        # item
        item = []

        # monster
        monsters = []

        ground1 = 65
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

        brick.append(object_class.object(48 * 108, ground1 + 60 * 2, 2))
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

        brick.append(object_class.object(48 * 151 - 37, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 - 5, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 + 27, ground1 + 60 + 20, 2))
        brick.append(object_class.object(48 * 151 + 32 * 2 - 5, ground1 + 60 + 20, 2))

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
            for i in range(0, k):
                Steelblock.append(object_class.object(48 * 200 - 32 * i, ground1 + 32 * 8 - 32 * k - 10, 98))

        item.append(object_class.object_item(48 * 3, ground1 - 15, 300))
        item.append(object_class.object_item(48 * 4, ground1 - 15, 301))
        item.append(object_class.object_item(48 * 5, ground1 - 15, 302))
        item.append(object_class.object_item(48 * 6, ground1 - 15, 303))

        for i in grounds:
            game_world.add_object(i, 1)
        for i in coin:
            game_world.add_object(i, 1)
        for i in Qblock:
            game_world.add_object(i, 1)
        for i in brick:
            game_world.add_object(i, 1)
        for i in skbrick:
            game_world.add_object(i, 1)
        for i in Steelblock:
            game_world.add_object(i, 1)
        for i in item:
            game_world.add_object(i, 1)

