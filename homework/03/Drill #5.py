import turtle
import random

def restart():
    turtle.reset()
    
def move_up():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()
    turtle.right(90)

def move_right():
    turtle.forward(50)
    turtle.stamp()

def move_left():
    turtle.left(180)
    turtle.forward(50)
    turtle.stamp()
    turtle.right(180)

def move_down():
    turtle.right(90)
    turtle.forward(50)
    turtle.stamp()
    turtle.left(90)

turtle.shape('turtle')
turtle.onkey(move_up,"w")
turtle.onkey(move_down,"s")
turtle.onkey(move_right,"d")
turtle.onkey(move_left,"a")
turtle.onkey(restart,'Escape')
turtle.listen()
