from turtle import Turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(250, 200)
        self.hideturtle()
        self.score = 0
        self.max_score = 50
        self.upgrade_scoreboard()

    def upgrade_scoreboard(self):
        self.write(align="center", arg=f"Score {self.score} / {self.max_score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(align="center", arg="GAME OVER",font=("Courier", 36, "normal") )

    def add_point(self):
        self.clear()
        self.score += 1
        self.upgrade_scoreboard()

