import random

hangman_database = ['konstantynopolitanczykowianeczka']
word = list(random.choice(hangman_database))

# declarations
if_contains = []
hangman = []
user_indexes = []
strikes = []
bank = []
repetition = False


# functions
def checking_letter(answer, indexes):
    for index, letter in enumerate(word):
        if letter == answer:
            indexes.append(index)
            if_contains.append(letter)


def initializing_list():
    for i in range(len(word)):
        hangman.append('-')
    print(''.join(hangman))


# starting program
initializing_list()

while True:
    user_try = input('Insert a letter: ')
    user_try = user_try.lower()
    checking_letter(user_try, user_indexes)

    # checking if word contains this letter
    if len(if_contains) == 0:
        strikes.append('1')
        print(f"You've made {len(strikes)} mistake(s)")

    # checking if user typed this letter before
    for tri in bank:
        if tri == user_try:
            repetition = True

    # condition statement if try another one, or run hangmaan
    if repetition:
        print("You've already typed this letter. Try another one")
    else:
        bank.append(user_try)  # appending to list 'bank' - helps with repetition check. Bank for all typed letters.
        for iterate_indexes in user_indexes:  # writting a letters at proper indexes
            hangman[int(iterate_indexes)] = user_try

        print(''.join(hangman))  # printing hangman as string

        if len(strikes) == 7:  # if player has made 7 mistakes, hangman is hang
            print('Unfortunately you lost :(')
            break
        if hangman == word:  # player won
            print('Congrats! You won the game :)')
            break

    # clearing used tables and booleans
    user_indexes = []
    if_contains = []
    repetition = False
