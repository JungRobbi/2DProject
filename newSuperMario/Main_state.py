from pico2d import *
import game_framework
import Title_state


from Map_def import *
from Mario_class import *

def enter(): # 생성
    global mario,map1, map2, stage

    stage = 1
    if stage == 1:
        mario = hero(50, 65)
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
    mapmove(mario)
    mario.update()

    for i in item:
        i.move()

    delay(0.001)

def draw():
    clear_canvas()
    if stage == 1:
        map1.clip_draw(0, 0, 4224, 624, 2110 * 2.5 + movex, 120 * 2.5 + movey, 4224 * 2.5, 624 * 2.5)
    elif stage == 2:
        map2.clip_draw(0, 0, 4224, 762, 2110 * 2.5 + movex, 378 * 2.5 + movey, 4224 * 2.5, 762 * 2.5)
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
    for m in goomba:
        m.draw()

    mario.draw()
    update_canvas()


def pause():
    pass

def resume():
    pass