from pico2d import *
import random
import game_world

balls = []
deleted_balls = []


class Ball:

    def __init__(self):
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('ball21x21.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = random.randint(25, get_canvas_width() - 25), random.randint(25, get_canvas_height() - 25)
        # get_canvas_width() // 2, get_canvas_height() // 2

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        pass

    def draw(self):
        self.font.draw(self.x - 20, self.y + 80, '(%d)' % (len(deleted_balls)), (255, 255, 0))
        self.image.draw(self.x, self.y)

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
            # deleted_balls[] += 1
        pass
