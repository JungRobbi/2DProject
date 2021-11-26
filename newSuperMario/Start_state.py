import game_framework
import Life_state
from object_variable import *
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    global marioLife
    image = load_image('Mario_credit.png')
    marioLife = 5

def exit():
    global image
    del(image)



def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.change_state(Life_state)
    logo_time += game_framework.frame_time

def draw():
    global image
    clear_canvas()
    image.clip_composite_draw(0, 0, 300, 168, 0, '', 512, 300,1024, 600)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




