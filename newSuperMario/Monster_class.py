from pico2d import *
import game_framework
from object_variable import *
import game_world
from BehaviorTree import *
import Main_state

def contact_aAndb(a, b, p = 0):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if p == 3:
        if left_a > right_b: return 0
        if right_a < left_b: return 0
    else:
        if left_a > right_b: return 0
        if right_a < left_b: return 0
        if top_a < bottom_b: return 0
        if bottom_a > top_b: return 0

    if top_a - (a.g + 5.0) * game_framework.frame_time < bottom_b: return 1 # 아래에서 위로
    if bottom_a + (a.g + 5.0) * game_framework.frame_time > top_b: return 2 # 위에서 아래로

    return 3 # 좌,우

class goomba:
    image = None
    def __init__(self, x, y, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.dir = dir
        self.frame = 0
        self.size = [40, 40]
        self.g = 0
        self.build_behavior_tree()
        if goomba.image == None:
            goomba.image = load_image('Monster.png')

    def update(self):
        self.bt.run()
        self.frame = (self.frame + 10 * game_framework.frame_time)
        if self.frame >= 9:
            self.frame = 0
        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y
        self.check()



    def move(self):
        self.move2x += self.dir * 0.9 * 100 * game_framework.frame_time
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        move_node = LeafNode("move", self.move)

        self.bt = BehaviorTree(move_node)


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 24, 1000 - 24, 24, 24, self.x, self.y, self.size[0], self.size[1])
        else:
            self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 24, 24, 24, 0, 'h', self.x, self.y,
                                           self.size[0], self.size[1])
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 13, self.y - 12, self.x + 13, self.y + 12

    def check(self):

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1

        for block in grounds:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1


class boo:
    image = None
    def __init__(self, x, y, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.dir = dir
        self.frame = 0
        self.size = [40, 40]
        self.g = 0
        self.build_behavior_tree()
        if boo.image == None:
            boo.image = load_image('Monster.png')

    def update(self):
        self.bt.run()
        self.frame = (self.frame + 10 * game_framework.frame_time)
        if self.frame >= 3:
            self.frame = 0
        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

    def find(self):
        # Main_state.get_mario().x
        distance = (Main_state.get_mario().x - self.x)**2 + (Main_state.get_mario().y - self.y)**2
        if distance < 500 ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def move_to_hero(self):
        dx = Main_state.get_mario().x - self.x
        dy = Main_state.get_mario().y - self.y
        if dx < 0:
            self.dir = -1
        else:
            self.dir = 1
        self.move2x += dx / 10 * 5 * game_framework.frame_time
        self.move2y += dy / 10 * 5 * game_framework.frame_time
        return BehaviorTree.SUCCESS


    def build_behavior_tree(self):
        find_node = LeafNode("find", self.find)
        move_to_hero_node = LeafNode("move_to_hero", self.move_to_hero)

        find_and_move_node = SequenceNode('find_and_move')
        find_and_move_node.add_children(find_node, move_to_hero_node)

        self.bt = BehaviorTree(find_and_move_node)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 24, 1000 - 2 * 24, 24, 24, self.x, self.y, self.size[0], self.size[1])
        else:
            self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 2 * 24, 24, 24, 0, 'h', self.x, self.y,
                                           self.size[0], self.size[1])
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 15, self.y + 15



class Hammer_bros:
    image = None
    def __init__(self, x, y, dir=1):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.dir = dir
        self.velocity = 1
        self.motion = 1
        self.frame = 0
        self.size = [40, 67]
        self.g = 0
        self.timer = 1.0

        self.build_behavior_tree()
        if Hammer_bros.image == None:
            Hammer_bros.image = load_image('Monster.png')

    def update(self):
        self.bt.run()
        self.frame = (self.frame + 10 * game_framework.frame_time)
        if self.velocity == 0:
            if self.frame >= 16:
                self.frame = 0
        else:
            if self.frame >= 25:
                self.frame = 0
        self.move2x += self.velocity * 0.9 * 100 * game_framework.frame_time
        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

        self.check()


    def draw(self):
        if self.dir == -1:
            if self.motion == 0:
                self.image.clip_draw(int(self.frame) * 24, 1000 - 2 * 24 - 88, 24, 48, self.x, self.y + 5, self.size[0],
                                     self.size[1] + 13)
            else:
                self.image.clip_draw(int(self.frame) * 24, 1000 - 2 * 24 - 40, 24, 40, self.x, self.y, self.size[0], self.size[1])
        else:
            if self.motion == 0:
                self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 2 * 24 - 88, 24, 48, 0, 'h', self.x, self.y + 5,
                                               self.size[0], self.size[1] + 13)
            else:
                self.image.clip_composite_draw(int(self.frame) * 24, 1000 - 2 * 24 - 40, 24, 40, 0, 'h', self.x, self.y,
                                           self.size[0], self.size[1])
        draw_rectangle(*self.get_bb())

    def find_and_see(self):
        distance = (Main_state.get_mario().x - self.x) ** 2 + (Main_state.get_mario().y - self.y) ** 2
        if distance < 300 ** 2:
            self.velocity = 0
            self.motion = 0
            dx = Main_state.get_mario().x - self.x
            if dx < 0:
                self.dir = -1
            else:
                self.dir = 1
            return BehaviorTree.SUCCESS
        else:
            self.velocity = self.dir
            self.motion = 1
            return BehaviorTree.FAIL

    def throwing(self):
        self.timer -= game_framework.frame_time

        if self.timer <= 0:
            self.timer = 1.0

            dx = Main_state.get_mario().x - self.x

            ham = Hammer(self.x - self.movex, self.y, 305, self.dir, dx)
            game_world.add_object(ham, 1)

            return BehaviorTree.SUCCESS

        return BehaviorTree.FAIL



    def build_behavior_tree(self):
        find_and_see_node = LeafNode("find_and_see", self.find_and_see)
        throwing_node = LeafNode("throwing", self.throwing)


        offense = SequenceNode('offense')
        offense.add_children(find_and_see_node, throwing_node)

        self.bt = BehaviorTree(offense)


    def get_bb(self):
        return self.x - 16, self.y - 35, self.x + 16, self.y + 20

    def check(self):

        for block in Qblock + brick + skbrick + Steelblock:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.velocity == 1:
                    self.velocity = -1
                    self.dir = -1
                else:
                    self.velocity = 1
                    self.dir = 1

        for block in grounds:  # 블럭
            if contact_aAndb(self, block) == 3:  # 좌우
                if self.velocity == 1:
                    self.velocity = -1
                    self.dir = -1
                else:
                    self.velocity = 1
                    self.dir = 1

class Hammer:
    image = None

    def __init__(self, x, y, ability=None, dir = 1, parabola):
        self.x = x
        self.y = y
        self.movex = 0
        self.move2x = 0
        self.movey = 0
        self.move2y = 0
        self.crex = x
        self.crey = y
        self.ability = ability
        self.dir = dir
        self.frame = 0
        self.JUMP = False
        self.ga = 5.0
        self.parabola = parabola

        self.py = 0


        self.size = [32, 32]
        if ability == 305:
            self.g = 500
            self.JUMP = True

        if Hammer.image == None:
            Hammer.image = load_image('Monster.png')
    def update(self):

        if self.ability == 305:
            self.frame = (self.frame + 60 * game_framework.frame_time)
            if self.frame >= 32:
                self.frame = 0

        self.py = self.move2y
        if self.ability >= 303:
            if self.JUMP:
                self.move2y += self.g * game_framework.frame_time
                self.g -= self.ga
                if self.g < 0:
                    self.JUMP = False

            else:
                self.move2y -= self.g * game_framework.frame_time
                self.g += self.ga
                if self.g >= 900 and self.ability == 303:
                    self.g = 900
        else:
            if self.JUMP:
                self.move2y += self.g * game_framework.frame_time
            else:
                self.move2y -= self.g * game_framework.frame_time

        if self.ability == 305:
            self.move2x += self.dir * 0.9 * self.parabola * game_framework.frame_time

        self.x = self.crex + self.movex + self.move2x
        self.y = self.crey + self.movey + self.move2y

        if self.y <= -50:
            game_world.remove_object(self)


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 16, 1000 - 2 * 24 - 112, 16, 16, self.x, self.y, self.size[0],
                                 self.size[1])
        else:
            self.image.clip_composite_draw(int(self.frame) * 16, 1000 - 2 * 24 - 112, 16, 16, 0, 'h', self.x,
                                           self.y,self.size[0], self.size[1])

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.ability == 304 :
            return self.x - 6, self.y - 6, self.x + 6, self.y + 6
        return self.x - 16, self.y - 16, self.x + 16, self.y + 14


