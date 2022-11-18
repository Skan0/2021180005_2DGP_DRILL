from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
def rec():
    y=90
    x=0
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)
    while(y < 560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.01)
    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.01)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.01)

def circle():
    degree = 0
    x=0
    y=0
    while(degree<4.5):
        #원의 중심 (400,325) 반지름 235
        y=235*math.sin(degree)
        x=235*math.cos(degree)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+x,320+y)
        degree+=0.05
        delay(0.03)

while(1):
    rec()
    circle()
close_canvas()
