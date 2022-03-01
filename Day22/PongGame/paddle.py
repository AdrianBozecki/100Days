from turtle import Turtle, Screen
STEP = 27

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def up(self):
        self.forward(STEP)

    def down(self):
        self.backward(STEP)

    def next_round(self, x):
        self.goto(x)
