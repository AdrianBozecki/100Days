import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from time import sleep
from random import randint

screen = Screen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
cars = []

for _ in range(13):
    car = CarManager()
    cars.append(car)

for i in range(1, len(cars)):
    cars[i].sety(cars[i - 1].ycor() - 40 - randint(-15, 15))

screen.listen()
screen.onkey(key="w", fun=player.up)
screen.onkey(key="s", fun=player.down)
game_is_on = True
round_is_on = True


def collision(obstacle):
    if player.distance(obstacle) < 20:
        scoreboard.game_over()
        return True


def next_round():
    sleep(1)
    player.next_round()
    scoreboard.next_round()
    for single in cars:
        single.next_round()


while game_is_on:
    time.sleep(0.1)

    for single_car in cars:
        if collision(single_car):
            round_is_on = False
            sleep(5)
            game_is_on = False
        if round_is_on:
            single_car.move()

    if player.ycor() > 290:
        round_is_on = False
        next_round()
        round_is_on = True

    screen.update()
