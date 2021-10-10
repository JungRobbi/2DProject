from pico2d import *


def handle_events():
    global running
    global dir
    global herodir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                herodir = 1
            elif event.key == SDLK_LEFT:
                dir += 1
                herodir = -1
    pass

def hero_sprites():
    if dir == 0: # 정지
        if herodir == 1:
            character.clip_draw(frame * 32, 960 - 40, 32, 40, x, 90)
        else:
            character.clip_composite_draw(frame * 32, 960 - 40, 32, 40, 0, 'h', x, 90, 32, 40)
    elif dir == 1: # 오른쪽 걸음
        character.clip_draw(frame * 32, 960, 32, 40, x, 90)
    elif dir == -1: # 왼쪽 걸음
        character.clip_composite_draw(frame * 32, 960, 32, 40, 0, 'h', x, 90, 32, 40)

open_canvas()

character = load_image('MarioMove.png')

running = True
x = 800 // 2

dir = 0 # LEFT = -1 RIGHT = 1
herodir = 1

frame = 0
speed = 0
framedir = 0

while running:
    clear_canvas()

    hero_sprites()

    update_canvas()

    handle_events()


    speed = (speed + 1) % 2
    # frame = (frame + speed) % 8

    if framedir == 0:
        frame = frame + speed
        if frame >= 4:
            framedir = 1
    else:
        frame = frame - speed
        if frame == 0:
            framedir = 0


    x += dir * 5
    delay(0.04)

close_canvas()


