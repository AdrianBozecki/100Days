from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")
list_of_states = list(data.state)

df = pandas.DataFrame.to_dict(data)

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.states_dict = df

    def show_state(self, name, x, y):
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{name}")

    def check_state(self, answer):
        for i in range(len(self.states_dict['state'])):
            if answer == self.states_dict['state'][i].lower():
                self.show_state(self.states_dict['state'][i], self.states_dict['x'][i], self.states_dict['y'][i])
                return True









