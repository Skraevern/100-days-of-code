from recipes import MENU
import os


def coffee_maker():
    os.system("cls||clear")
    
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money = 0
    user_input = ""

    def print_report():
            print(f'Water: {resources["water"]}')
            print(f'Milk: {resources["milk"]}')
            print(f'Coffee: {resources["coffee"]}')
            print(f"Money: ${money}")

    def check_resources(type_of_coffee):
        if resources["water"] - MENU[type_of_coffee]["ingredients"]["water"] < 0:
             return False
        elif resources["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"] < 0:
             return False
        elif "milk" in MENU[type_of_coffee]["ingredients"]:
            if resources["milk"] - MENU[type_of_coffee]["ingredients"]["milk"] < 0:
                return False
            else:
                 return True
        else:
             return True
             
    while user_input != "off":
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "report":
            print_report()
        elif user_input in MENU:
             enough_resources = check_resources(user_input)
             print(enough_resources)
             if enough_resources:
                  print("Please insert coins.")
#                   quarters =
#                   dimes =
#                   nickles =
#                   pennies = 
# How many quarters?: 12
# How many dimes?: 12
# How many nickles?: 12
# How many pennies?: 12 
# Here is you $2.42 in change.
# Here is your latte ☕️ Enjoy!
        # TODO 3. Process coins
        # TODO 4. Check transaction succesfull
        # TODO 5. Make coffee




coffee_maker()