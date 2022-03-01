from turtle import Turtle
from random import randint
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y = randint(250, 400)
        self.x = 350
        self.move_speed = 1

    def wall_bounce(self):
        self.y = -self.y

    def paddle_bounce(self):
        self.x = - self.x
        self.move_speed *= 1.02
        self.x *= self.move_speed

    def ball_detection(self, paddle):
        if abs(self.xcor() - paddle.xcor()) < 5 and abs(self.ycor() - paddle.ycor()) < 50:
            return True

    def next_round(self):
        self.x = 350
        self.move_speed = 1
        self.y = randint(250, 450)
        self.x = self.x * (-1)
        self.goto(0, 0)

    def move(self):
        new_coord = (self.xcor() + self.x / 100, self.ycor() + self.y / 100)
        self.goto(new_coord)
        sleep(0.01)

    def game(self, left ,right):
        if 360 > self.xcor() > - 360:
            if self.ycor() > 280 or self.ycor() < -280:
                self.wall_bounce()
            if self.ball_detection(right) or self.ball_detection(left):
                self.paddle_bounce()
            self.move()
        else:
            return True


  #  def reset(self):

