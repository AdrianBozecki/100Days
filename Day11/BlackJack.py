import random

cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'As': 11,
}


def random_card():  # random picking elements from list
    return random.choice(list(cards))


def result(points):  # calculating point out of list/dict
    points_sum = 0
    for name in points:
        if name == 'As':  # As is 1 or 11 depends on conditions
            if points_sum > 10:
                points_sum += 1
            else:
                points_sum += 11
        else:
            points_sum += cards[name]
    return points_sum


def deal(pick):  # appending a card on certain deal
    pick.append(random_card())


def outcome(player_hand, dealer_hand):  # final result
    print("\nResult:\n")
    print(f"Player's final hand : {player_hand}, final score = {result(player_hand)}")
    print(f"Dealer's final hand : {dealer_hand}, final score = {result(dealer_hand)}")


game_over = False  # variables to work on loops
next_game = True

while next_game:
    while not game_over:
        print('WELCOME TO BLACKJACK GAME')
        player_cards = True
        dealer_cards = True
        dealer = False
        player = False
        dealers_hand = []  # empty lists to store a cards
        players_hand = []
        for i in range(2):  # first hand
            deal(dealers_hand)
            deal(players_hand)
        print("First Deal:")
        print(f"Dealer's first card : ['{dealers_hand[0]}']")
        print(f"Player's cards : {players_hand}, score = {result(players_hand)}")

        while player_cards:  # taking cards as a player untill its < 21
            answer = input('Do you want to take card?\n')
            if answer == 'y':
                deal(players_hand)
                print(f"Player's cards : {players_hand}, score = {result(players_hand)}")
            elif answer == 'n':
                player_cards = False
            if result(players_hand) > 21:
                dealer = True
                player_cards = False

        if dealer:  # if dealer is true means that player already passed 21, end of game
            outcome(players_hand, dealers_hand)
            print('Dealer Wins')
            break

        while dealer_cards:  # if player didn't pass 21, dealer is taking cards untill he will have >17 points
            if result(dealers_hand) < 17:
                deal(dealers_hand)
                print(f"Dealer : {dealers_hand}, score = {result(dealers_hand)}")
            elif result(dealers_hand) > 21:
                player = True
                dealer_cards = False
            else:
                dealer_cards = False

        if player:  # if player is true means that dealer already passed 21, and he lost, end of game
            outcome(players_hand, dealers_hand)
            print('Player Wins')
            break

        outcome(players_hand, dealers_hand)  # if anybody passed 21, we have to check who is closer to 21
        if result(players_hand) > result(dealers_hand):
            print('Player Wins')
        elif result(players_hand) < result(dealers_hand):
            print('Dealer Wins')
        else:
            print('Draw')

        game_over = True  # ending a loop with the game

    decision = input('\nDo you want to play next game?\n')
    if decision == 'y':
        game_over = False
    elif decision == 'n':
        print('Bye bye !!!')
        next_game = False
