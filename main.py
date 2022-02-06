import random
import turtle as t
from turtle import Screen

scr = Screen()
tim = t
# tim.shape("circle")
t.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

tim.pensize(9)
tim.speed(5)

for a in range(1000):
    directions = [0, 90, 180, 270]
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))

scr.exitonclick()
