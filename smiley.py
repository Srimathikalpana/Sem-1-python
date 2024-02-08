import turtle

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_smiley_face():
    draw_circle(0, 0, 100, "yellow")
    draw_circle(-40, 120, 20, "black")
    draw_circle(40, 120, 20, "black")
    turtle.penup()
    turtle.goto(0, 80)
    turtle.pendown()
    turtle.setheading(270)
    turtle.width(8)
    turtle.circle(10, 200)

turtle.speed(0.5)
draw_smiley_face()
turtle.done()
