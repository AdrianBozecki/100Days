from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(800, 600)

user_bet = screen.textinput("BET", "Who will win? Type a color:")
colors = ["red", "green", "blue", "brown", "black"]
y_positions = [200, 100, 0, -100, -200]
all_turtles = []


for index in range(5):
    adi = Turtle(shape="turtle")
    adi.color(colors[index])
    adi.penup()
    adi.goto(-350, y_positions[index])
    all_turtles.append(adi)



def move(ob):
    ob.forward(randint(5, 15))

end_of_game = False

while not end_of_game:
    for obj in all_turtles:
        move(obj)
        if obj.xcor() >= 350:
            print(f"The winner is {obj.fillcolor()}")
            if obj.fillcolor() == user_bet.lower():
                print(f"You've won! The winning turtle is {obj.fillcolor()}")
            else:
                print(f"You've lost! The winning turtle is {obj.fillcolor()}")
            end_of_game = True

screen.exitonclick()
