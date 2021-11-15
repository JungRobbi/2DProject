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
    contact_ALLcheck(mario)
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.001)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def contact_ALLcheck(mario):
    Qblock_sizex = 16
    Qblock_sizey = 16
    mario.py = -100
    for game_object in game_world.all_objects():
        if mario.grow == 0 and game_object:
            if (mario.x - 16 <= game_object.x + (14.4)) and (
                    mario.x + 16 >= game_object.x - (14.4)) and (
                    mario.y - 32 <= game_object.y + (12.8)) and (
                    mario.y + 8 >= game_object.y - (16) and (
                    game_object.ability >= 300 and game_object.ability < 400
            )):
                if game_object.ability == 300:
                    mario.grow = 1
                    game_object.ability = -1

            elif (mario.x - 16 <= game_object.x + (Qblock_sizex)) and (
                    mario.x + 16 >= game_object.x - (Qblock_sizex)) and (
                    mario.y - 32 <= game_object.y + (Qblock_sizey)) and (
                    mario.y + 8 >= game_object.y - (Qblock_sizey) and (
                    game_object.ability < 110 and game_object.ability >= 100
            )):

                mario.x -= mario.dir * mario.xspeed
                if mario.dir == 0:
                    mario.x -= mario.herodir * mario.xspeed

                if mario.status == 1:
                    game_object.ability = 111
                    game_object.frame = 0
                    game_object.fs = 0

                    mario.y -= mario.g
                    mario.g = mario.g + mario.ga
                    mario.status = -1
                elif mario.status == -1:
                    mario.py = game_object.y + (Qblock_sizey) + 33
                    mario.y = mario.py
                    mario.status = 0
                    mario.g = 4.5
                    mario.frame = 0



            elif (mario.x - 16 <= game_object.x + (game_object.size[0])) and (
                    mario.x + 16 >= game_object.x - (game_object.size[0])) and (
                    mario.y - 32 <= game_object.y + (game_object.size[1])) and (
                    mario.y + 8 >= game_object.y - (game_object.size[1]) and (
                    game_object.ability == 999  # ground
            )):
                mario.x -= mario.dir * mario.xspeed
                if mario.dir == 0:
                    mario.x -= mario.herodir * mario.xspeed

                if mario.status == 1:
                    mario.status = -1
                elif mario.status == -1:
                    mario.py = game_object.y + (game_object.size[1]) + 33
                    mario.y = mario.py
                    mario.status = 0
                    mario.g = 4.5
                    mario.frame = 0


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

