from pico2d import *

class hero:

    def __init__(self, d, h, s, f, fd, x):
        self.dir = d
        self.herodir = h
        self.speed = s
        self.frame = f
        self.framedir = fd
        self.x = x

    def handle_events(self):
        global running

        self.events = get_events()
        for event in self.events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir += 1
                elif event.key == SDLK_LEFT:
                    self.dir -= 1
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
        if self.dir == 0:  # 정지
            if self.herodir == 1:
                character.clip_draw(self.frame * 32, 960 - 40, 32, 40, self.x, 90)
            else:
                character.clip_composite_draw(self.frame * 32, 960 - 40, 32, 40, 0, 'h', self.x, 90, 32, 40)
        elif self.dir == 1:  # 오른쪽 걸음
            character.clip_draw(self.frame * 32, 960, 32, 40, self.x, 90)
        elif self.dir == -1:  # 왼쪽 걸음
            character.clip_composite_draw(self.frame * 32, 960, 32, 40, 0, 'h', self.x, 90, 32, 40)

        self.speed = (self.speed + 1) % 2
        if self.framedir == 0:
            self.frame = self.frame + self.speed
            if self.frame >= 4:
                self.framedir = 1
        else:
            self.frame = self.frame - self.speed
            if self.frame == 0:
                self.framedir = 0

    def move(self):
        self.x += self.dir * 5

    pass



open_canvas()

character = load_image('MarioMove.png')

running = True

mario = hero(0, 0, 0, 0, 0, 800 // 2)

while running:
    clear_canvas()

    mario.sprites()

    update_canvas()

    mario.handle_events()
    mario.move()

    delay(0.04)

close_canvas()


