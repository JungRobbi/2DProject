import game_framework
import game_world
import Main_state
import end_state
from object_variable import *
from pico2d import *


name = "LifeState"
image = None
Num_image_white = None
Num_image_black = None
logo_time = 0.0

global line
global data

def enter():
    global image, Num_image_white, Num_image_black
    global line, data

    game_world.clear()

    Num_image_black = load_image('font_Black.png')
    Num_image_white = load_image('font_White.png')
    image = load_image('Life_image.png')

    f = open("Life.txt", 'r')
    line = f.readline()
    data = int(line)
    f.close()

def exit():
    global image

    del(image)



def update():
    global logo_time
    global line, data

    f = open("Life.txt", 'r')
    line = f.readline()
    data = int(line)
    f.close()

    if (logo_time > 3.0):
        logo_time = 0
        game_framework.change_state(Main_state)

    logo_time += game_framework.frame_time

def draw():
    global image
    global line, data
    global image, Num_image_white, Num_image_black

    clear_canvas()
    image.clip_composite_draw(0, 0, 1024, 600, 0, '', 512, 300, 1024, 600)

    Num_image_white.clip_composite_draw(24 + data * 110, 286, 64, 64, 0, '', 590, 237,64, 64)

    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass