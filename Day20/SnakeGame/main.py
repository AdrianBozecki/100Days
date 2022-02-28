from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def game_over():
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        print("game_over")
        scoreboard.game_over()
        return True


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(n=0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="d", fun=snake.east)
screen.onkey(key="w", fun=snake.north)
screen.onkey(key="a", fun=snake.west)
screen.onkey(key="s", fun=snake.south)

end_of_game = False
while not end_of_game:
    screen.update()
    snake.move()
    sleep(0.1)
    # detect collision with food
    if snake.head.distance(food) <= 1:
        food.refresh()
        scoreboard.refresh()
        snake.extend()
    # detect collision with wall
    if game_over():
        end_of_game = True
    # detect collisin with tail
    for tail in snake.list_of_turtles:
        if tail == snake.head:
            pass
        elif snake.head.distance(tail) < 10:
            scoreboard.game_over()
            end_of_game = True
            print("siema")

screen.exitonclick()
