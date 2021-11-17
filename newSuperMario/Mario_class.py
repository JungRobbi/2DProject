from pico2d import *
import game_framework

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,\
UP_DOWN, UP_UP, DOWN_DOWN, DOWN_UP,\
STOP_RUN, STOP_UP, STOP_DOWN = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 21

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

        hero.fs_deel = 8


    def exit(hero, event):
        pass

    def do(hero):
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if hero.grow == 0:
            if hero.y > hero.py:
                if hero.frame > 20:
                    hero.frame = 20
            else:
                if hero.frame > 21:
                    hero.frame = 0
        elif hero.grow == 1:
            if hero.y > hero.py:
                if hero.frame > 19:
                    hero.frame = 19
            else:
                if hero.frame > 23:
                    hero.frame = 0

        if hero.xspeed > 0:
            hero.xspeed -= hero.xa * 5
        if hero.xspeed < 0:
            hero.xspeed = 0
        hero.x += hero.dir * hero.xspeed * game_framework.frame_time

        if hero.JUMP:
            hero.y += hero.g * game_framework.frame_time
            hero.g = hero.g - hero.ga
            if hero.g <= 0:
                hero.JUMP = False
        else:
            if hero.y > hero.py:
                hero.y -= hero.g * game_framework.frame_time
                hero.g = hero.g + hero.ga
                if hero.g > 900:
                    hero.g = 900
            elif hero.y <= hero.py:
                hero.y = hero.py

    def draw(hero):
        if hero.grow == 1:  # 성장 후
            if hero.y > hero.py:
                if hero.dir == 1:
                    hero.image.clip_draw(int(hero.frame) * 32, 1000 - 4 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                         hero.size[1])
                elif hero.dir == -1:
                    hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 4 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                   hero.size[0], hero.size[1])
            else:
                if hero.dir == 1:
                    hero.image.clip_draw(int(hero.frame) * 32, 1000 - 1 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                         hero.size[1])
                else:
                    hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 1 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                   hero.size[0], hero.size[1])
        elif hero.grow == 0:  # 성장 전
            if hero.y > hero.py:
                if hero.dir == 1:
                    hero.image.clip_draw(int(hero.frame) * 32, 1000 - 18 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                         hero.size[1])
                elif hero.dir == -1:
                    hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 18 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                   hero.size[0], hero.size[1])
            else:
                if hero.dir == 1:
                    hero.image.clip_draw(int(hero.frame) * 32, 1000 - 15 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                         hero.size[1])
                else:
                    hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 15 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                   hero.size[0], hero.size[1])



class RunState:

    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.velocity += 1
            hero.dir = 1
            hero.collect += 1
            hero.xspeed = 0
        elif event == LEFT_DOWN:
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
        hero.velocity = clamp(-1, hero.velocity, 1)

    def exit(hero, event):
        pass

    def do(hero):
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

        elif hero.grow == 1:
            if hero.y > hero.py:
                if hero.frame > 19:
                    hero.frame = 19
            else:
                if hero.frame > 10 and hero.xspeed == hero.xMAX:
                    hero.frame = 0

                if hero.frame > 27:
                    hero.frame = 4

        hero.x += hero.velocity * hero.xspeed * game_framework.frame_time
        if hero.xspeed < hero.xMAX:
            hero.xspeed += hero.xa
        elif hero.xspeed > hero.xMAX:
            hero.xspeed = hero.xMAX
            hero.frame = 0

            # x 이동
        if hero.collect == 0:
            hero.add_event(STOP_RUN)

        if hero.JUMP:
            hero.y += hero.g * game_framework.frame_time
            hero.g = hero.g - hero.ga
            if hero.g <= 0:
                hero.JUMP = False
        else:
            if hero.y > hero.py:
                hero.y -= hero.g * game_framework.frame_time
                hero.g = hero.g + hero.ga
                if hero.g > 900:
                    hero.g = 900
            elif hero.y <= hero.py:
                hero.y = hero.py

    def draw(hero):
        if hero.grow == 1:  # 성장 후
            if hero.y > hero.py:
                if hero.dir == 1:
                    hero.image.clip_draw(int(hero.frame) * 32, 1000 - 4 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                         hero.size[1])
                elif hero.dir == -1:
                    hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 4 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                   hero.size[0], hero.size[1])
            else:
                if hero.dir == 1:  # 오른쪽 걸음
                    if hero.xspeed == hero.xMAX:
                        hero.image.clip_draw(int(hero.frame) * 32, 1000 - 3 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    else:
                        hero.image.clip_draw(int(hero.frame) * 32, 1000 - 2 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                elif hero.dir == -1:  # 왼쪽 걸음
                    if hero.xspeed == hero.xMAX:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 3 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                    else:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 2 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])

        elif hero.grow == 0:  # 성장 전
            if hero.y > hero.py:
                if hero.dir == 1:
                    hero.image.clip_draw(int(hero.frame) * 32, 1000 - 18 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                         hero.size[1])
                elif hero.dir == -1:
                    hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 18 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                   hero.size[0], hero.size[1])
            else:
                if hero.dir == 1:  # 오른쪽 걸음
                    if hero.xspeed == hero.xMAX:
                        hero.image.clip_draw(int(hero.frame) * 32, 1000 - 17 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                    else:
                        hero.image.clip_draw(int(hero.frame) * 32, 1000 - 16 * 40, 32, 40, hero.x, hero.y, hero.size[0],
                                             hero.size[1])
                elif hero.dir == -1:  # 왼쪽 걸음
                    if hero.xspeed == hero.xMAX:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 17 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])
                    else:
                        hero.image.clip_composite_draw(int(hero.frame) * 32, 1000 - 16 * 40, 32, 40, 0, 'h', hero.x, hero.y,
                                                       hero.size[0], hero.size[1])



next_state_table = {
IdleState:{RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: IdleState, LEFT_UP: IdleState,
           UP_DOWN: IdleState, UP_UP: IdleState, DOWN_DOWN: IdleState, DOWN_UP: IdleState,
           STOP_RUN: IdleState},
RunState:{RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: RunState, LEFT_UP: RunState,
          UP_DOWN: RunState, UP_UP: RunState, DOWN_DOWN: RunState, DOWN_UP: RunState,
          STOP_RUN: IdleState},
}

class hero:
    image = None

    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.dir = 1
        self.JUMP = False
        self.velocity = 0
        self.collect = 0
        self.xspeed = 0
        self.xMAX = 600.0
        self.xa = 4.0
        self.frame = 0
        self.fs = 0
        self.fs_deel = 0
        self.py = 50
        self.g = 900
        self.ga = 9.8
        self.size = [64, 80]
        self.grow = 0
        self.sit = 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

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
            return self.x - 16, self.y - 40, self.x + 16, self.y + 8
        return self.x - 16, self.y - 40, self.x + 16, self.y + 28
