import game_framework
import pico2d

import Start_state
import Main_state

pico2d.open_canvas(1024, 600)
game_framework.run(Main_state)
pico2d.close_canvas()