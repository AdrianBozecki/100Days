from random import randint

print('Welcome to the Number Guessing Game!')
print("I'm thinking of number between 1 and 100.")
diff_level = input("Choose difficulty level. Type 'easy' or 'hard':\n")
game_off = False

if diff_level == 'easy':
    attempts = 10
elif diff_level == 'hard':
    attempts = 5
else:
    print('Try again')

the_number = randint(1, 100)

while not game_off:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess:\n"))
    attempts -= 1

    if guess == the_number:
        print(f"You got it! The answer was {the_number}")
        game_off = True
    elif guess < the_number:
        print("Too low.\nGuess again.\n")
    elif guess > the_number:
        print("Too high.\nGuess again.\n")

    if attempts == 0:
        print(f"You lost! The answer was {the_number}")
        game_off = True
