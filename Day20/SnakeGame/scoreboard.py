from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.message = f"Score = {self.score}"
        self.update_scoreboard()

    def refresh(self):
        self.clear()
        self.score += 1
        self.message = f"Score = {self.score}"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.message, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour score is {self.score}",align="center", font=("Arial", 40, "normal"))
