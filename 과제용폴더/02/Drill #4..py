import turtle
int i=0

while i<6:
    turtle.penup()
    turtle.goto(i*100,500)
    turtle.pendown()
    turtle.goto(i*100,0)
    i=i+1
while i<6:
    turtle.penup()
    turtle.goto(0,i*100)
    turtle.pendown()
    turtle.goto(500,i*100)
    i=i+1
