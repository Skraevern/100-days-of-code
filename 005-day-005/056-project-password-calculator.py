import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '/', '(', ')', '_', '-', '+', '=', '}', '{', ']', '[', '|', ':', ';', ',', '<', '>', '.', '?']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = ""

print("Welcome to password creator!")
password_length = int(input("How long do you want the password do be? "))
symbol_choice = input("Should the password contain symbols? Y or N ").lower()
number_choice = input("Should the password contain numbers? Y or N ").lower()



for i in range(1, password_length):
    character_list_random = random.randint(0, 4)
    if character_list_random == 0 and symbol_choice == "y":
        character_random = random.randint(0, len(symbols) - 1)
        password += symbols[character_random]
    elif character_list_random == 1 and number_choice == "y":
        character_random = random.randint(0, len(numbers) - 1)
        password += numbers[character_random]
    else:
        character_random = random.randint(0, len(alphabet) - 1)
        password += alphabet[character_random]

print(password)
        