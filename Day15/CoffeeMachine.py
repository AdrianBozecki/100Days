from CoffeeMachineData import MENU
from CoffeeMachineData import resources


def report():
    print("Actual level of resources:")
    print(f"water : {resources['ingredients']['water']}ml")
    print(f"milk : {resources['ingredients']['milk']}ml")
    print(f"coffee : {resources['ingredients']['coffee']}g")
    print(f"cost : ${resources['cost']}")


def checking_resources(types):
    for i in resources["ingredients"]:
        if resources['ingredients'][i] < MENU[types]["ingredients"][i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def using_resources(types):
    for i in resources["ingredients"]:
        resources['ingredients'][i] -= MENU[types]["ingredients"][i]


def paying(set):
    summ = 0
    print("Please insert coins.")
    quarters = int(input('How many quarters?:'))
    dimes = int(input('How many dimes?:'))
    nickles = int(input('How many nickles?:'))
    pennys = int(input('How many pennys?: '))
    given_coins = [quarters, dimes, nickles, pennys]
    value = [0.25, 0.1, 0.05, 0.01]
    for i in range(len(value)):
        summ += value[i] * given_coins[i]
    summ -= MENU[set]["cost"]
    return round(summ, 2)


def make_coffee(set):
    if checking_resources(set):
        price = paying(set)
        if price >= 0:
            using_resources(set)
            resources["cost"] += MENU[set]["cost"]
            print(f"Here is in change &{price}")
            print(f"Here is your {set}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")

end = False
while not end:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'espresso' :
        make_coffee('espresso')
    elif choice == 'latte':
        make_coffee('latte')
    elif choice == 'cappuccino':
        make_coffee('cappuccino')
    elif choice == 'report':
        report()
    elif choice == 'end':
        print("Thank you for visit")
        end = True


