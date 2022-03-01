from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        xcor = randint(-14, 14) * 20
        ycor = randint(-14, 14) * 20
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5)
        self.goto(xcor, ycor)
        self.speed("fastest")

    def refresh(self):
        xcor = randint(-14, 14) * 20
        ycor = randint(-14, 14) * 20
        self.goto(xcor, ycor)


