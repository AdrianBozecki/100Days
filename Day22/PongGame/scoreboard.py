from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.first_score = 0
        self.second_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.message = f"{self.second_score} : {self.first_score}"
        self.write(self.message, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nFinal score is {self.first_score} : {self.second_score}", align="center", font=("Arial", 40, "normal"))

    def update_scoreboard(self, x_coord):
        self.clear()
        if x_coord > 360:
            self.first_score += 1
        elif x_coord < - 360:
            self.second_score += 1
        self.message = f"{self.first_score} : {self.second_score}"
        self.write(self.message, align=ALIGNMENT, font=FONT)