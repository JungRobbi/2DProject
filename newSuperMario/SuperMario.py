import game_framework
import pico2d

import Start_state
import Main_state

pico2d.open_canvas(1100, 616)
game_framework.run(Main_state)
pico2d.close_canvas()