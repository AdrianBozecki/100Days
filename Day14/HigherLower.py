from HigherLowerData import data
from random import randint

count = 0
end_of_game = False


def right_pick(a, b):
    if a > b:
        c = 'A'
    elif a < b:
        c = 'B'
    return c

first_pick = data[randint(0, len(data) - 1)]

while not end_of_game:

    second_pick = data[randint(0, len(data))]
    if second_pick == first_pick:
        second_pick = data[randint(0, len(data))]

    print(f"\nCompare A: {first_pick['name']}, {first_pick['description']}, {first_pick['country']}\nVS")
    print(f"Against B: {second_pick['name']}, {second_pick['description']}, {second_pick['country']}\n")

    answear = input("Who has more followers? Type 'A' or 'B': ")
    right_answer = right_pick(first_pick['follower_count'], second_pick['follower_count'])

    if answear != right_answer:
        print(f"Sorry, that's wrong. Final score:  {count}")
        end_of_game = True
    else:
        count += 1
        print(f"You're right! Current score: {count}")
        first_pick = second_pick








