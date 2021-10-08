from pico2d import *


def handle_events():
    global running
    global dir

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
            elif event.key == SDLK_LEFT:
                dir += 1
    pass

open_canvas()

character = load_image('Mario.gif')

running = True
x = 800 // 2

dir = 0 # LEFT = -1 RIGHT = 1

frame = 0

while running:
    clear_canvas()

    character.clip_draw(frame * 15, 23 * 7, 23, 23, x, 90)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.10)

close_canvas()

