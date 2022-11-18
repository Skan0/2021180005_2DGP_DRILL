from pico2d import*
import boy_grass_object
import title_state
import game_framework
import item_state
boy = None
grass = None
running = None
class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None

def update(self):
    self.frame = (self.frame + 1) % 8
    self.x += 1
def enter():
    global boy, grass, running
    boy = Boy()
    grass = boy_grass_object.Grass()
    running = True

def exit():
    global boy, grass
    del boy
    del grass

def draw_world():
    grass.draw()
    boy.draw()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw(self):
    self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    if self.item == 'BigBall':
        self.big_ball_image.draw(self.x+10, self.y+50)
    elif self.item == 'Ball':
        self.ball_image.draw(self.x+10, self.y+50)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)



open_canvas()

enter()
# game main loop code
while running:
    boy_grass_object.handle_events()
    update()
    draw()
exit()
# finalization code
close_canvas()