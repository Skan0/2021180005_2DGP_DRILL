import math
from pico2d import*
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.1)
    

def run_rectangle():
    for x in range(50,750+1,10):
        render_all(x,90)
            

def run_circle():
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)
    cx, cy, r = 400, 300, 200
    for deg in range(0,360,5):
        x=cx+r*math.cos(deg/360*2*math.pi)
        y=cy+r*math.sin(deg/360*2*math.pi)
        render_all(x,y)

while True:
    run_rectangle()
    run_circle()
  
    break
close_canvas()
