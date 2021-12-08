import game_framework
from pico2d import *


name = "EndState"
image = None
logo_time = 0.0
sound = None
data = None

def enter():
    global image, sound, data

    f = open("Stage.txt", 'r')
    line = f.readline()
    data = int(line)
    f.close()


    if data == 1:
        image = load_image('win.png')
        sound = load_music('clear_game.mp3')
        sound.set_volume(64)
        sound.play()
    else:
        image = load_image('gameover.png')
        sound = load_music('gameover.mp3')
        sound.set_volume(64)
        sound.play()


def exit():
    global image, sound, data
    del(image)
    del(sound)
    del(data)



def update():
    global logo_time
    if (logo_time > 7.0):
        logo_time = 0
        game_framework.quit()
    logo_time += game_framework.frame_time

def draw():
    global image, data
    clear_canvas()
    if not data == 1:
        image.clip_composite_draw(0, 0, 975, 1042, 0, '', 512, 300,1024, 1000)
    else:
        image.clip_composite_draw(0, 0, 801, 997, 0, '', 512, 300, 1024, 1000)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




