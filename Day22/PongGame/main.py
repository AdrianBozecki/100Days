from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.tracer(n=0)

screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

def next_round():
    ball.next_round()
    l_paddle.next_round((-350, 0))
    r_paddle.next_round((350, 0))
#while not end_of_game:
end_of_round = False
# moving ball

while not end_of_round:
    if ball.game(l_paddle, r_paddle):
        scoreboard.update_scoreboard(ball.xcor())
        sleep(2)
        next_round()
        if scoreboard.first_score == 5 or scoreboard.second_score == 5:
            scoreboard.game_over()
            end_of_round = True
    screen.update()













screen.exitonclick()