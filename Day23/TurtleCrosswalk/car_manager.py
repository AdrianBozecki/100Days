from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10
STARTING_POSITION_Y = 260
STARTING_POSITION_X = (60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440)
RESET = (300, 310, 320, 315, 305)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto((random.choice(STARTING_POSITION_X), STARTING_POSITION_Y))
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_speed)
        if self.xcor() <= - 300:
            self.setx(random.choice(RESET))

    def next_round(self):
        self.move_speed += MOVE_INCREMENT
        self.setx(random.choice(STARTING_POSITION_X))





