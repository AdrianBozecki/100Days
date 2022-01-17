import random
from Hangman_art import stages, logo
from Hanhman_words import word_list

word = list(random.choice(word_list))

# declarations
display = []
lives = 6
end_of_game = False

# functions
def checking_letter(guess):
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = guess


def initializing():
    for i in word:
        display.append('-')
    print(''.join(display))
    print(logo)


# starting program
initializing()

while not end_of_game:
    user_try = input('Insert a letter: ').lower()

    if user_try in display:
        print(f"You've already guessed {user_try} letter before")
    checking_letter(user_try)

    print(''.join(display))  # printing hangman as string

    # checking if word contains this letter
    if user_try not in word:
        lives -= 1
        print(f"You guessed {user_try}, that's not in the word. You lose a life.")
        if lives == 0:  # if player has made 7 mistakes, hangman is hang
            print('Unfortunately you lost :(')
            end_of_game = True

    if display == word:  # player won
        print('Congrats! You won the game :)')
        end_of_game = True

    print(f"{stages[lives]}")

