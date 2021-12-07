import random

from pico2d import *

import Main_state
import game_framework
from object_variable import *
import game_world
import object_class

import Life_state
import Start_state
import end_state

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,\
UP_DOWN, UP_UP, DOWN_DOWN, DOWN_UP,\
STOP_RUN, STOP_UP, STOP_DOWN, DIE, SPACE, CLEAR = range(14)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 21

DEL_TIME = 1
temp_grow = 0
temp2_grow = 0

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

# Boy States

class IdleState:

    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.velocity += 1
            hero.collect += 1
            hero.xspeed = 0
        elif event == LEFT_DOWN:
            hero.velocity -= 1
            hero.collect += 1
            hero.xspeed = 0
        elif event == RIGHT_UP:
            hero.velocity -= 1
            hero.collect -= 1
        elif event == LEFT_UP:
            hero.velocity += 1
            hero.collect -= 1
        elif event == UP_DOWN and hero.y == hero.py:
            hero.JUMP = True
            hero.frame = 0
            hero.g = 1100
            hero.sit = 0
            if hero.grow == 0:
                hero.mini_jump.play()
            else:
                hero.jump.play()

        elif event == DOWN_DOWN and not hero.JUMP:
            hero.sit = 1
            hero.frame = 0
        elif event == DOWN_UP:
            hero.sit = 0

        hero.fs_deel = 8


    def exit(hero, event):
        if event == SPACE:
            hero.fire_ball()

    def do(hero):
        global DEL_TIME
        global temp_grow, temp2_grow

        if DEL_TIME <= 1:
            DEL_TIME += game_framework.frame_time
            if hero.grow == 0:
                if hero.y > hero.py:
                    if hero.frame > 20:
                        hero.frame = 20
                else:
                    if hero.frame > 21:
                        hero.frame = 0
            elif hero.grow >= 1:
                if hero.y > hero.py:
                    if hero.frame > 19:
                        hero.frame = 19
                else:
                    if hero.frame > 23:
                        hero.frame = 0

            if DEL_TIME <= 0.1:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.2:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.3:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.4:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.5:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.6:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.7:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.8:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.9:
                hero.grow = temp2_grow

            if DEL_TIME > 1:
                hero.grow = temp_grow
                temp_grow = 0
                temp2_grow = 0
        else:
            if hero.startimer > 0:
                if hero.startimer < 0.2:
                    hero.star.stop()
                    hero.bgm.repeat_play()
                hero.startimer -= game_framework.frame_time

            if hero.sit == 1:
                hero.frame = (hero.frame + game_framework.frame_time * 18)
            else:
                hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)


            if hero.grow == 0:
                if hero.y > hero.py:
                    if hero.frame > 20:
                        hero.frame = 20
                else:
                    if hero.frame > 21:
                        hero.frame = 0
                    if hero.sit == 1:
                        if hero.frame > 2:
                            hero.frame = 2
            elif hero.grow >= 1:
                if hero.y > hero.py:
                    if hero.frame > 19:
                        hero.frame = 19
                else:
                    if hero.frame > 23:
                        hero.frame = 0
                    if hero.sit == 1:
                        if hero.frame > 2:
                            hero.frame = 2

            if hero.xspeed > 0:
                hero.xspeed -= hero.xa * 5
            if hero.xspeed < 0:
                hero.xspeed = 0
            hero.x += hero.dir * hero.xspeed * game_framework.frame_time
            hero.movex += hero.dir * hero.xspeed * game_framework.frame_time

            if hero.JUMP:
                hero.y += clamp(-3, hero.g * game_framework.frame_time, 3)
                hero.g = hero.g - hero.ga
                if hero.g <= 0:
                    hero.JUMP = False
            else:
                if hero.y > hero.py:
                    hero.y -= clamp(-3, hero.g * game_framework.frame_time, 3)
                    hero.g = hero.g + hero.ga
                    if hero.g > 1100:
                        hero.g = 1100
                elif hero.y <= hero.py:
                    hero.y = hero.py

            if hero.y <= 0:
                hero.add_event(DIE)
                hero.g = 1100.0
                DEL_TIME = 0
                hero.JUMP = True
                hero.frame = 0

            global BOOL_CLEAR
            if BOOL_CLEAR:
                hero.add_event(CLEAR)
                hero.frame = 0

    def draw(hero):
        if hero.IVtimer > 0 and int(hero.frame) % 2 == 1: pass
        else:
            if hero.grow >= 1:  # 성장 후
                if hero.sit == 1:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 5 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    elif hero.dir == -1:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 5 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                elif hero.y > hero.py:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 4 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    elif hero.dir == -1:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 4 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                else:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 1 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    else:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 1 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
            elif hero.grow == 0:  # 성장 전

                if hero.sit == 1:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 19 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    elif hero.dir == -1:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 19 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                elif hero.y > hero.py:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 18 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    elif hero.dir == -1:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 18 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                else:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 15 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    else:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 15 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])



class RunState:

    def enter(hero, event):
        if event == RIGHT_DOWN:
            if hero.dir == -1:
                hero.x += hero.xMAX * game_framework.frame_time
            hero.velocity += 1
            hero.dir = 1
            hero.collect += 1
            hero.xspeed = 0
        elif event == LEFT_DOWN:
            if hero.dir == 1:
                hero.x -= hero.xMAX * game_framework.frame_time
            hero.velocity -= 1
            hero.dir = -1
            hero.collect += 1
            hero.xspeed = 0
        elif event == RIGHT_UP:
            hero.velocity -= 1
            if hero.collect == 2:
                hero.dir = -1
            hero.collect -= 1
        elif event == LEFT_UP:
            hero.velocity += 1
            if hero.collect == 2:
                hero.dir = 1
            hero.collect -= 1
        elif event == UP_DOWN and hero.y == hero.py:
            hero.JUMP = True
            hero.frame = 0
            hero.g = 1100

            if hero.grow == 0:
                hero.mini_jump.play()
            else:
                hero.jump.play()

        hero.sit = 0


        hero.velocity = clamp(-1, hero.velocity, 1)


    def exit(hero, event):
        if event == SPACE:
            hero.fire_ball()

    def do(hero):
        global DEL_TIME
        global temp_grow, temp2_grow

        if DEL_TIME <= 1:
            DEL_TIME += game_framework.frame_time
            if hero.grow == 0:
                if hero.y > hero.py:
                    if hero.frame > 20:
                        hero.frame = 20
                else:
                    if hero.frame > 9 and hero.xspeed == hero.xMAX:
                        hero.frame = 0

                    if hero.frame > 22:
                        hero.frame = 0

            elif hero.grow >= 1:
                if hero.y > hero.py:
                    if hero.frame > 19:
                        hero.frame = 19
                else:
                    if hero.frame > 10 and hero.xspeed == hero.xMAX:
                        hero.frame = 0

                    if hero.frame > 27:
                        hero.frame = 4

            if DEL_TIME <= 0.1:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.2:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.3:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.4:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.5:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.6:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.7:
                hero.grow = temp2_grow
            elif DEL_TIME <= 0.8:
                hero.grow = temp_grow
            elif DEL_TIME <= 0.9:
                hero.grow = temp2_grow

            if DEL_TIME > 1:
                hero.grow = temp_grow
                temp_grow = 0
                temp2_grow = 0
        else:
            if hero.startimer > 0:
                if hero.startimer < 0.2:
                    hero.star.stop()
                    hero.bgm.repeat_play()
                hero.startimer -= game_framework.frame_time
            if hero.sit == 1:
                hero.frame = (hero.frame + game_framework.frame_time * 18)
            else:
                hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)


            if hero.grow == 0:
                if hero.y > hero.py:
                    if hero.frame > 20:
                        hero.frame = 20
                else:
                    if hero.frame > 9 and hero.xspeed == hero.xMAX:
                        hero.frame = 0

                    if hero.frame > 22:
                        hero.frame = 0

            elif hero.grow >= 1:
                if hero.y > hero.py:
                    if hero.frame > 19:
                        hero.frame = 19
                else:
                    if hero.frame > 10 and hero.xspeed == hero.xMAX:
                        hero.frame = 0

                    if hero.frame > 27:
                        hero.frame = 4

            hero.x += hero.velocity * hero.xspeed * game_framework.frame_time
            hero.movex += hero.velocity * hero.xspeed * game_framework.frame_time
            if hero.xspeed < hero.xMAX:
                hero.xspeed += hero.xa
            elif hero.xspeed > hero.xMAX:
                hero.xspeed = hero.xMAX
                hero.frame = 0

                # x 이동
            if hero.collect == 0:
                hero.add_event(STOP_RUN)

            if hero.JUMP:
                hero.y += clamp(-3, hero.g * game_framework.frame_time, 3)
                hero.g = hero.g - hero.ga
                if hero.g <= 0:
                    hero.JUMP = False
            else:
                if hero.y > hero.py:
                    hero.y -= clamp(-3, hero.g * game_framework.frame_time, 3)
                    hero.g = hero.g + hero.ga
                    if hero.g > 1100:
                        hero.g = 1100
                elif hero.y <= hero.py:
                    hero.y = hero.py
                    hero.g = 0

            if hero.y <= 0:
                hero.add_event(DIE)
                hero.g = 1100.0
                DEL_TIME = 0
                hero.JUMP = True
                hero.frame = 0

            global BOOL_CLEAR
            if BOOL_CLEAR:
                hero.add_event(CLEAR)
                hero.frame = 0

    def draw(hero):
        if hero.IVtimer > 0 and int(hero.frame) % 2 == 1: pass
        else:
            if hero.grow >= 1:  # 성장 후
                if hero.y > hero.py:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 4 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    elif hero.dir == -1:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 4 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                else:
                    if hero.dir == 1:  # 오른쪽 걸음
                        if hero.xspeed == hero.xMAX:
                            hero.image.clip_draw(int(hero.frame) * 32, 2000 - 3 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                                 hero.size[1])
                        else:
                            hero.image.clip_draw(int(hero.frame) * 32, 2000 - 2 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                                 hero.size[1])
                    elif hero.dir == -1:  # 왼쪽 걸음
                        if hero.xspeed == hero.xMAX:
                            hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 3 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                           hero.size[0], hero.size[1])
                        else:
                            hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 2 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                           hero.size[0], hero.size[1])

            elif hero.grow == 0:  # 성장 전
                if hero.y > hero.py:
                    if hero.dir == 1:
                        hero.image.clip_draw(int(hero.frame) * 32, 2000 - 18 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    elif hero.dir == -1:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 18 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                else:
                    if hero.dir == 1:  # 오른쪽 걸음
                        if hero.xspeed == hero.xMAX:
                            hero.image.clip_draw(int(hero.frame) * 32, 2000 - 17 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                                 hero.size[1])
                        else:
                            hero.image.clip_draw(int(hero.frame) * 32, 2000 - 16 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                                 hero.size[1])
                    elif hero.dir == -1:  # 왼쪽 걸음
                        if hero.xspeed == hero.xMAX:
                            hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 17 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                           hero.size[0], hero.size[1])
                        else:
                            hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 16 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                           hero.size[0], hero.size[1])

class DieState:
    def enter(hero, event):
        global TIME_PER_ACTION, ACTION_PER_TIME, FRAMES_PER_ACTION, DEL_TIME
        if hero.grow == 0:
            TIME_PER_ACTION = 0.7
            ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
            FRAMES_PER_ACTION = 3
        elif hero.grow >= 1:
            TIME_PER_ACTION = 0.7
            ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
            FRAMES_PER_ACTION = 13

        if event == DIE:
            hero.bgm.stop()
            hero.bgm = load_music('lifelost.mp3')
            hero.bgm.set_volume(48)
            hero.bgm.play(1)



    def exit(hero, event):
        pass

    def do(hero):
        global DEL_TIME, CHANGE_TIME, CHANGE_INOUT
        global TIME_PER_ACTION, ACTION_PER_TIME, FRAMES_PER_ACTION

        DEL_TIME += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if DEL_TIME <= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * 20:
            hero.y += hero.g * game_framework.frame_time
        elif DEL_TIME >= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * 140:
            hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
            if hero.frame > 13 and hero.grow >= 1:
                hero.frame = 0
            elif hero.frame > 3 and hero.grow == 0:
                hero.frame = 0

            if hero.JUMP:
                hero.y += hero.g * game_framework.frame_time
                hero.g = hero.g - hero.ga
                if hero.g <= 0:
                    hero.JUMP = False
            else:
                hero.y -= hero.g * game_framework.frame_time
                hero.g = hero.g + hero.ga
                if hero.g > 1100:
                    hero.g = 1100
                    CHANGE_TIME = 1.0
                if hero.y <= -500:
                    TIME_PER_ACTION = 0.7
                    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
                    FRAMES_PER_ACTION = 21
                    DEL_TIME = 1

                    f = open("Life.txt", 'r')
                    line = f.readline()
                    data = int(line)
                    f.close()

                    if data == 0:
                        game_framework.change_state(end_state)
                    else:
                        game_framework.change_state(Life_state)

                    f = open("Life.txt", 'w')
                    data -= 1
                    f.write(str(data))
                    f.close()



    def draw(hero):
        if hero.grow >= 1:  # 성장 후
            hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 7 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                           hero.size[0], hero.size[1])
        elif hero.grow == 0:  # 성장 전
            hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 21 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                           hero.size[0], hero.size[1])

class ClearState:
    def enter(hero, event):
        if event == CLEAR:
            hero.bgm.stop()
            hero.clear.play(1)

    def exit(hero, event):
        pass

    def do(hero):
        hero.frame = (hero.frame + 15 * game_framework.frame_time)

        if hero.frame > 22:
            hero.frame = 22

        hero.x += 300.0 * game_framework.frame_time
        hero.y += 300.0 * game_framework.frame_time

        if hero.y >= 1000:
            game_framework.change_state(Life_state)  # 다음 장면
            f = open("Stage.txt", 'r')
            line = f.readline()
            data = int(line)
            f.close()

            f = open("Stage.txt", 'w')
            data += 1
            f.write(str(data))
            f.close()

            hero.x = 40
            hero.y = 300
            hero.add_event(STOP_RUN)
            hero.SET_BLOCK = None
            hero.velocity = 0
            hero.JUMP = False
            global BOOL_CLEAR
            BOOL_CLEAR = False





    def draw(hero):
        hero.image.clip_composite_draw(int(hero.frame) * 32, 2000 - 10 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                       hero.size[0], hero.size[1])


next_state_table = {
IdleState:{RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: IdleState, LEFT_UP: IdleState,
           UP_DOWN: IdleState, UP_UP: IdleState, DOWN_DOWN: IdleState, DOWN_UP: IdleState,
           STOP_RUN: IdleState, DIE: DieState , SPACE: IdleState, CLEAR: ClearState},
RunState:{RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: RunState, LEFT_UP: RunState,
          UP_DOWN: RunState, UP_UP: RunState, DOWN_DOWN: IdleState, DOWN_UP: RunState,
          STOP_RUN: IdleState, DIE: DieState , SPACE: RunState, CLEAR: ClearState},
DieState:{RIGHT_DOWN: DieState, LEFT_DOWN: DieState, RIGHT_UP: DieState, LEFT_UP: DieState,
          UP_DOWN: DieState, UP_UP: DieState, DOWN_DOWN: DieState, DOWN_UP: DieState,
          STOP_RUN: IdleState, DIE: DieState, SPACE: DieState, CLEAR: ClearState},
ClearState:{RIGHT_DOWN: ClearState, LEFT_DOWN: ClearState, RIGHT_UP: ClearState, LEFT_UP: ClearState,
          UP_DOWN: ClearState, UP_UP: ClearState, DOWN_DOWN: ClearState, DOWN_UP: ClearState,
          STOP_RUN: IdleState, DIE: ClearState, SPACE: ClearState, CLEAR: ClearState}
}

class hero:
    image = None

    def __init__(self,x, y, round):
        self.crex = x
        self.crey = y
        self.movex = 0
        self.x = x
        self.y = y
        self.dir = 1
        self.JUMP = False
        self.velocity = 0
        self.collect = 0
        self.xspeed = 0
        self.xMAX = 500.0
        self.xa = 4.0
        self.frame = 0
        self.fs = 0
        self.fs_deel = 0
        self.py = 50
        self.g = 1100
        self.ga = 9.8
        self.size = [64, 80]
        self.grow = 0
        self.sit = 0
        self.SET_BLOCK = None
        self.IVtimer = 0.0
        self.score = 0

        self.startimer = 0.0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        if round == 1:
            self.bgm = load_music('round2.mp3')
        else:
            self.bgm = load_music('round1.mp3')
        self.bgm.set_volume(48)
        self.bgm.repeat_play()

        self.star = load_music('starman.mp3')
        self.bgm.set_volume(48)

        self.eat_coin = load_wav('coin.wav')
        self.eat_coin.set_volume(64)

        self.eat_grow = load_wav('grow.wav')
        self.eat_grow.set_volume(64)

        self.jump = load_wav('jump.wav')
        self.jump.set_volume(64)

        self.mini_jump = load_wav('mini_jump.wav')
        self.mini_jump.set_volume(512)

        self.fireball = load_wav('fireball.wav')
        self.fireball.set_volume(64)

        self.crush_block = load_wav('crush_block.wav')
        self.crush_block.set_volume(32)

        self.clear = load_wav('clear_round.wav')
        self.clear.set_volume(128)


        if hero.image == None:
            hero.image = load_image('MarioMove.png')

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            try:
                self.cur_state.exit(self, event)
                self.cur_state = next_state_table[self.cur_state][event]
                self.cur_state.enter(self, event)
            except:
                print("state : ", self.cur_state, "event :", event)
                exit(-1)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

        # debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))

    def get_bb(self):
        if self.grow == 0:
            if self.sit == 1:
                return self.x - 16, self.y - 40, self.x + 16, self.y - 10
            return self.x - 16, self.y - 40, self.x + 16, self.y + 8
        if self.sit == 1:
            return self.x - 16, self.y - 40, self.x + 16, self.y - 6
        return self.x - 16, self.y - 40, self.x + 16, self.y + 28

    def check(self):
        global SET_BLOCK
        global DEL_TIME
        global temp_grow, temp2_grow
        global BOOL_CLEAR

        if not BOOL_CLEAR and not self.cur_state == DieState:
            for eat in coin + item:  # 먹으면 사라지는 객체
                if contact_aAndb(self, eat) > 0:
                    if eat.ability == 0:
                        self.eat_coin.play()
                        coin.remove(eat)
                        self.score += 1
                    elif eat.ability >= 300 and eat.ability <= 304:
                        if eat.ability == 300:  # 버섯
                            if self.grow < 1:
                                self.eat_grow.play()
                                DEL_TIME = 0
                                temp2_grow = self.grow
                                temp_grow = 1
                        elif eat.ability == 302:  # 꽃
                            if self.grow < 2:
                                self.eat_grow.play()
                                DEL_TIME = 0
                                temp2_grow = self.grow
                                temp_grow = 2
                        elif eat.ability == 303:  # 별
                            self.bgm.pause()
                            self.star.play()
                            self.startimer = 10.0
                        else: # 파란버섯
                            self.eat_grow.play()
                            DEL_TIME = 0
                            temp2_grow = self.grow
                            temp_grow = random.randint(0, 100) % 3



                        item.remove(eat)
                    game_world.remove_object(eat)

            for block in Qblock + brick + skbrick + Steelblock:  # 블럭
                if contact_aAndb(self, block) == 2:  # 위서 아래로
                    if self.py < block.y + block.size[1] + 3:
                        self.py = block.y + block.size[1] + 3
                    if block.ability == 99:
                        self.py = block.y + block.size[1]
                    SET_BLOCK = block
                elif contact_aAndb(self, block) == 3:  # 좌우
                    self.x -= self.velocity * self.xspeed * game_framework.frame_time
                    if self.cur_state == IdleState and self.velocity == 0:
                        self.x -= self.dir * self.xspeed * game_framework.frame_time
                elif contact_aAndb(self, block) == 1:  # 아래서 위로
                    self.JUMP = False
                    if block.ability >= 100 and block.ability <= 109:
                        if block.ability == 100:
                            t = object_class.debris(block.crex, block.crey + 24, 201)
                            t.movex = block.movex
                            t.movey = block.movey
                            game_world.add_object(t, 1)
                            self.score += 1
                            self.eat_coin.play()

                        if block.ability >= 101:
                            t = object_class.object_item(block.crex, block.crey + 25, 1299 + (block.ability % 100))
                            t.movex = block.movex
                            t.movey = block.movey
                            t.set_block = block
                            t.frame = 0
                            item.append(t)
                            game_world.add_object(t, 1)

                        block.ability = block.ability + 10
                        block.frame = 0
                        block.fs = 0

                    if block.ability == 4:
                        block.ability = 5
                    elif block.ability == 5:
                        block.ability = 4

                    if block.ability == 2 and self.grow >= 1:
                        if block in brick:
                            brick.remove(block)
                        game_world.remove_object(block)
                        self.crush_block.play()

                        t = object_class.debris(block.crex - 5, block.crey, 200, 1, 1)
                        t.movex = block.movex
                        t.movey = block.movey
                        game_world.add_object(t, 1)

                        t = object_class.debris(block.crex + 5, block.crey, 200, -1)
                        t.movex = block.movex
                        t.movey = block.movey
                        game_world.add_object(t, 1)

                        t = object_class.debris(block.crex, block.crey + 20, 200, 1, 1)
                        t.movex = block.movex
                        t.movey = block.movey
                        game_world.add_object(t, 1)

                        t = object_class.debris(block.crex, block.crey + 20, 200, -1)
                        t.movex = block.movex
                        t.movey = block.movey
                        game_world.add_object(t, 1)

                    if block.ability == 3:
                        self.score += 1
                        self.eat_coin.play()
                        t = object_class.debris(block.crex, block.crey + 24, 201)
                        t.movex = block.movex
                        t.movey = block.movey
                        game_world.add_object(t, 1)


            for block in grounds:  # 블럭
                if contact_aAndb(self, block) == 2:  # 위서 아래로
                    if self.py < block.y + block.size[1] + self.size[1] / 2 + 1:
                        self.py = block.y + block.size[1] + self.size[1] / 2 + 1
                    SET_BLOCK = block
                elif contact_aAndb(self, block) == 3:  # 좌우
                    self.x -= self.velocity * self.xspeed * game_framework.frame_time
                    if self.cur_state == IdleState and self.velocity == 0:
                        self.x -= self.dir * self.xspeed * game_framework.frame_time


                    if block.ability == 950: # 깃발
                        BOOL_CLEAR = True
                elif contact_aAndb(self, block) == 1:  # 아래서 위로
                    self.JUMP = False

            for block in monsters:  # 몬스터
                for att in game_world.all_objects():
                    if att.__class__.__name__ == "object_item" and att.ability == 304:
                        if contact_aAndb(block, att) > 0:
                            block.die = True
                            block.timer = 1.0
                if self.startimer > 0 and contact_aAndb(self, block) > 0:
                    block.die = True
                    block.timer = 1.0

                if block.die == False:
                    if contact_aAndb(self, block) == 2:  # 위서 아래로
                        if block.__class__.__name__ == "plant":
                            if self.startimer <= 0:

                                if self.grow > 0:
                                    self.grow -= 1
                                    self.IVtimer = 1.0
                                else:
                                    self.add_event(DIE)
                                    self.g = 1100.0
                                    DEL_TIME = 0
                                    self.JUMP = True
                                    self.frame = 0
                        else:
                            self.JUMP = True
                            self.g = 400
                            block.die = True
                            block.timer = 1.0
                    elif contact_aAndb(self, block) == 3:  # 좌우
                        if self.startimer <= 0:
                            if self.grow > 0:
                                self.grow -= 1
                                self.IVtimer = 1.0
                            else:
                                self.add_event(DIE)
                                self.g = 1100.0
                                DEL_TIME = 0
                                self.JUMP = True
                                self.frame = 0
                    elif contact_aAndb(self, block) == 1:  # 아래서 위로
                        if self.startimer <= 0:
                            if self.grow > 0:
                                self.grow -= 1
                                self.IVtimer = 1.0
                            else:
                                self.add_event(DIE)
                                self.g = 1100.0
                                DEL_TIME = 0
                                self.JUMP = True
                                self.frame = 0

            for block in game_world.all_objects():  # 몬스터 공격
                if block.__class__.__name__ == "Hammer":
                    if contact_aAndb(self, block) > 0:
                        if self.startimer <= 0:
                            if self.grow > 0:
                                self.grow -= 1
                                self.IVtimer = 1.0
                            else:
                                self.add_event(DIE)
                                self.g = 1100.0
                                DEL_TIME = 0
                                self.JUMP = True
                                self.frame = 0

            if not SET_BLOCK == None:
                if not contact_aAndb(self, SET_BLOCK, 3) > 0:
                    self.py = 0

    def fire_ball(self):
        if self.grow == 2:
            self.fireball.play()
            ball = object_class.object_item(self.x - self.movex, self.y, 304, self.dir)
            game_world.add_object(ball, 1)