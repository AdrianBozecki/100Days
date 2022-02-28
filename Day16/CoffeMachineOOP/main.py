from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
end = False


def raport():
    coffee_maker.report()
    money_machine.report()


def make_coffee(option):
    drink = menu.find_drink(option)
    if coffee_maker.is_resource_sufficient(drink):
        money_machine.make_payment(drink.cost)
        coffee_maker.make_coffee(drink)


while not end:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == 'report':
        raport()
    elif choice == 'off':
        end = True
    elif choice in menu.get_items():
        make_coffee(choice)
    else:
        print("We don't have that in our menu")



