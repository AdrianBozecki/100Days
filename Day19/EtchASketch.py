from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def clockwise():
    tim.right(10)


def counterclockwise():
    tim.right(-10)


def clear():
    tim.penup()
    tim.clear()
    tim.goto(0,0)
    tim.pendown()
    tim.setheading(0)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
