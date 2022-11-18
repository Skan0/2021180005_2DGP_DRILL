from pico2d import *
import random
import game_world
import game_framework

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(10,700), random.randint(200, 500)
        self.velocity = random.randint(0, 7)
        self.locate = 1
    def draw(self):
        if self.locate == 1:
            if self.x <= 1600 - 100:
                self.image.clip_composite_draw(int(self.velocity)*100, int(self.y), 100, 100, self.x, self.y)
        else :
            
        # self.clip_composite_draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
