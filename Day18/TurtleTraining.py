from turtle import Turtle, colormode
from turtle import Screen
from random import choice, randint

colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.width(1)
tim.speed(100)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    t = (r, g, b)
    return t


def shapes(sides):
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)

# from triangle to decagon
# for i in range(3,10):
#     tim.color(choice(colors))
#     shapes(i)

# random walk
# direction = [0, 90, 180, 270]
#
# for _ in range(1000):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.right(choice(direction))

#spirograph
def spirograph(amount_of_circles = 72, size = 120):
    for _ in range(amount_of_circles):
        tim.circle(size)
        tim.pencolor(random_color())
        tim.right(360/amount_of_circles)

spirograph()

screen = Screen()
screen.exitonclick()