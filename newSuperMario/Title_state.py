import game_framework
import Life_state
import Mario_class
from object_variable import *
from pico2d import *


name = "TitleState"
image = None
sound = None

def enter():
    global image, sound
    image = load_image('Mario_title.png')
    sound = load_music('title.mp3')
    sound.set_volume(64)
    sound.repeat_play()

    f = open("Life.txt", 'w')
    data = "4"
    f.write(data)
    f.close()

    f = open("Stage.txt", 'w')
    data = "0"
    f.write(data)
    f.close()

def exit():
    global image, sound
    del(image)
    sound.stop()
    del(sound)




def update():
  pass



def draw():
    global image
    clear_canvas()
    image.clip_composite_draw(0, 0, 900, 506, 0, '', 512, 300,1024, 600)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(Life_state)



def pause(): pass


def resume(): pass




