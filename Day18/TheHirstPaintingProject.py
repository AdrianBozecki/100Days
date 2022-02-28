from turtle import Turtle, colormode
from turtle import Screen
from random import choice
import colorgram

# extracting colors from image
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.b
#     b = i.rgb.g
#     color=(r, g, b)
#     rgb_colors.append(color)
# print(rgb_colors)
color_list = [(202, 110, 164), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]

colormode(255)
tim = Turtle()
tim.width(1)
tim.speed(100)
tim.penup()
tim.hideturtle()

tim.setpos(-300, - 300)
for i in range(1, 101):
    tim.pendown()
    tim.dot(20, choice(color_list))
    tim.penup()
    tim.forward(50)
    if i % 10 == 0:
        coord = tim.pos()
        tim.setpos(coord[0] - 500, coord[1] + 50)


screen = Screen()
screen.exitonclick()