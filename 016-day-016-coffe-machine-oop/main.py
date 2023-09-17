from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
machine_on = True
money_machine = MoneyMachine()

while machine_on:
    user_input = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_input == "report":
        machine.report()
        money_machine.report()
    elif user_input == "off":
        machine_on = False
    elif menu.find_drink(user_input) != None:
        drink = menu.find_drink(user_input)
        if machine.is_resource_sufficient(drink):
            payment_accepted = False
            while payment_accepted == False:
                print(f"{drink.name.title()} costs ${drink.cost}")
                payment_accepted = money_machine.make_payment(drink.cost)
            machine.make_coffee(drink)
            




