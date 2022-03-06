import turtle
from states import States
from scoreboard import Scoreboard
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
pic = "blank_states_img.gif"
screen.setup(760, 520)
screen.bgpic(pic)
screen.tracer(n=0)
states = States()
scoreboard = Scoreboard()

#Making list of all states
list_of_states = []
guessed_states = []
missing_states = []
for st in states.states_dict['state']:
    list_of_states.append(states.states_dict['state'][st])



end_of_game = False
while not end_of_game:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state == 'exit':
        end_of_game = True
    if states.check_state(answer_state):
        scoreboard.add_point()
        guessed_states.append(answer_state.capitalize())


for i in range(len(list_of_states)):
    if list_of_states[i] in guessed_states:
        pass
    else:
        missing_states.append(list_of_states[i])

ms = pandas.DataFrame(missing_states)
ms.to_csv("missing_states.csv")


screen.exitonclick()