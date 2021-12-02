import game_framework
import game_world
import Main_state
from object_variable import *
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0
marioLife = 5

def enter():
    global image, ROUND
    global marioLife
    
    game_world.clear()


    image = load_image('Life_image.png')

def exit():
    global image
    del(image)



def update():
    global logo_time
    if (logo_time > 3.0):
        logo_time = 0
        game_framework.change_state(Main_state)
    logo_time += game_framework.frame_time

def draw():
    global image, ROUND
    clear_canvas()
    if ROUND == 1:
        image.clip_composite_draw(0, 0, 1024, 600, 0, '', 512, 300,1024, 600)
    else:
        image.clip_composite_draw(0, 0, 1024, 600, 0, '', 512, 300, 1024, 600)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass