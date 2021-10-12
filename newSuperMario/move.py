from pico2d import *

class hero:
    dir = 0
    herodir = 0
    status = 0
    speed = 0
    frame = 0
    framedir = 0
    py = 0
    jump_power = 350
    g = 0.0
    gn = 0

    def __init__(self,x, y):
        self.x = x
        self.y = y
    def handle_events(self):
        global running

        self.events = get_events()
        for event in self.events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir += 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_LEFT:
                    self.dir -= 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_UP and self.status == 0:
                    self.g = 0.0
                    self.gn = 0
                    self.py = self.y
                    self.status = 1
                    self.frame = 0
                    self.framedir = 0
                elif event.key == SDLK_DOWN:
                    self.status = 0
                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                    self.herodir = 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
                    self.herodir = -1
        pass

    def sprites(self):
        if self.status != 0: # 점프 등의 특수 상태
           if self.dir == 0:  # 정지
               if self.herodir == 1:
                   character.clip_draw(self.frame * 32, 960 - 2 * 40, 32, 40, self.x, self.y, 64, 80)
               else:
                   character.clip_composite_draw(self.frame * 32, 960 - 2 * 40, 32, 40, 0, 'h', self.x, self.y, 64, 80)
           if self.dir == 1:
               character.clip_draw(self.frame * 32, 960 - 2 * 40, 32, 40, self.x, self.y, 64, 80)
           elif self.dir == -1:
               character.clip_composite_draw(self.frame * 32, 960 - 2 * 40, 32, 40, 0, 'h', self.x, self.y, 64, 80)
        else: # 기본 이동 스프라이트
           if self.dir == 0:  # 정지
               if self.herodir == 1:
                   character.clip_draw(self.frame * 32, 960 - 40, 32, 40, self.x, self.y, 64, 80)
               else:
                   character.clip_composite_draw(self.frame * 32, 960 - 40, 32, 40, 0, 'h', self.x, self.y, 64, 80)
           elif self.dir == 1:  # 오른쪽 걸음
               character.clip_draw(self.frame * 32, 960, 32, 40, self.x, self.y, 64, 80)
           elif self.dir == -1:  # 왼쪽 걸음
               character.clip_composite_draw(self.frame * 32, 960, 32, 40, 0, 'h', self.x, self.y, 64, 80)




        self.speed = (self.speed + 1) % 2


        if self.framedir == 0:
            self.frame = self.frame + self.speed
            if self.status == 1 or self.status == -1:
                if self.frame > 4:
                    self.frame = self.frame - self.speed
            elif self.dir == -1 or self.dir == 1:  # 나머지 프레임
                if self.frame >= 4:
                    self.framedir = 1
            elif self.dir == 0 and self.status == 0:
                if self.frame >= 9: # 정지 프레임
                    self.frame = 0
        else:
            self.frame = self.frame - self.speed
            if self.frame == 0:
                self.framedir = 0

    def move(self):
        if self.status == 1:
            self.y = (1 - self.g)*self.py + self.g*(self.py+ self.jump_power)
            self.g += (1 - self.g) / 15
            self.gn += 1
            if self.gn > 24:
                self.status = -1
        elif self.status == -1:
            self.y = (1 - self.g)*self.py + self.g*(self.py+ self.jump_power)
            self.g -= (1 - self.g) / 15
            self.gn -= 1
            if self.gn < -2:
                self.y = self.py
                self.gn = 0
                self.status = 0



        self.x += self.dir * 8

    pass



open_canvas(1024, 800)

character = load_image('MarioMove.png')

running = True

mario = hero(800 // 2, 90)

while running:
    clear_canvas()

    mario.sprites()

    update_canvas()

    mario.handle_events()
    mario.move()

    delay(0.025)

close_canvas()


