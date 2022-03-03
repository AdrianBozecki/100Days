from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.level = 1
        self.upgrade_scoreboard()

    def upgrade_scoreboard(self):
        self.write(f"Level : {self.level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(align = "center", arg="GAME OVER",font=("Courier", 36, "normal") )

    def next_round(self):
        self.clear()
        self.level += 1
        self.upgrade_scoreboard()

