import os

game_on = True
dictionary = {}
all_players = []
winners_bid = 0
winner = 'none'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def appending_new_bidders(name, bid, new_dictionary):
    new_dictionary['name'] = name
    new_dictionary['bid'] = bid


print("Welcome to the secret auction program.")

while game_on :
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    appending_new_bidders(name, bid, dictionary)
    all_players.append(dictionary)
    dictionary = {}
    other_bidders = input("Are There any other bidders? Type 'yes' or 'no'")
    clear_screen()

    if other_bidders == 'no':
        for player in all_players:
            if player['bid'] > winners_bid:
                winners_bid = player['bid']
                winner = player['name']
        print(f'The winner is {winner}, with {winners_bid}$ bid')
        game_on = False