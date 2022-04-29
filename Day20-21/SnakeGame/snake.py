from turtle import Turtle

SNAKE_X_COORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.list_of_turtles = []
        self.create_snake()
        self.head = self.list_of_turtles[0]

    def create_snake(self):
        for position in SNAKE_X_COORDS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.goto(position)
        new_turtle.penup()
        new_turtle.resizemode("user")
        new_turtle.color("white")
        self.list_of_turtles.append(new_turtle)

    def extend(self):
        self.add_segment((self.list_of_turtles[-1].position()))

    def north(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def east(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def west(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def south(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def move(self):
        size = len(self.list_of_turtles) - 1
        for seg_num in range(size, 0, -1):
            new_x = self.list_of_turtles[seg_num - 1].xcor()
            new_y = self.list_of_turtles[seg_num - 1].ycor()
            self.list_of_turtles[seg_num].goto(new_x, new_y)
        self.list_of_turtles[0].forward(MOVE_DISTANCE)
