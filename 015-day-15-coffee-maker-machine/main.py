from recipes import MENU
import os

def coffee_maker():
    os.system("cls||clear")
    
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
    user_input = ""


    def print_report():
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${resources["money"]}')

    def update_resources(resources):
        resources["water"] += int(input(f'Enter filled WATER amount in ml: '))
        resources["milk"] += int(input(f'Enter filled MILK amount in ml: '))
        resources["coffee"] += int(input(f'Enter filled COFFEE amount in grams: '))
        resources["money"] -= int(input(f'Enter removed MONEY amount: '))
        return resources

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
             
    def check_coins(total_coins, user_input):
        total = total_coins
        print(f'{user_input.title()} costs ${MENU[user_input]["cost"]}')
        print(f"Total inserted ${total}")
        if total > 0:
             print(f'remaining ${round(MENU[user_input]["cost"] - total, 2)}')
        print("Please insert coins.")
        total += (0.25 * int(input("How many quarters?: ")))
        total += (0.10 * int(input("How many dimes?: ")))
        total += (0.05 * int(input("How many nickles?: ")))
        total += (0.01 * int(input("How many pennies?: ")))
        return round(total, 2)

    def make_coffee(resources):
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        if "milk" in MENU[user_input]["ingredients"]:
            resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        return resources
    
    print("Enter s for settings.")
    while user_input != "off":
        user_input = ""
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "s":
            settings_input1 = ""
            settings_input2 = ""
            while settings_input1 != "q":
                settings_input1 = input("q to quit. Password: ")
                if settings_input1 == "1234":
                    settings_input2 = input('Type "report" or "update": ')
                    if settings_input2 == "report":
                        print_report()
                    if settings_input2 == "update":
                        resources = update_resources(resources)
        elif user_input in MENU:
            if check_resources(user_input):
                total_coins = 0
                while total_coins < MENU[user_input]["cost"]:
                    total_coins = check_coins(total_coins, user_input)
                change = total_coins - MENU[user_input]["cost"]
                resources["money"] += MENU[user_input]["cost"]
                resources = make_coffee(resources)
                if change > 0:
                    print(f'Here is your ${change} in change.')
                print(f"Here is your {user_input.title()} ☕️ Enjoy!")
            else:
                print(f'{user_input.title()} is out of stock. Please try another or type "off" to quit')

coffee_maker()