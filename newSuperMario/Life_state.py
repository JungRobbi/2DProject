import game_framework
import Main_state
from pico2d import *


name = "StartState"
image = None
life = None
logo_time = 0.0


def enter():
    global image; global life
    # image = load_image('')

def exit():
    global image
    del(image)



def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.change_state(Main_state)
    logo_time += game_framework.frame_time

def draw():
    global image
    clear_canvas()
    # image.clip_composite_draw(0, 0, 300, 168, 0, '', 512, 300,1024, 600)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass