import random
from lists import alphabet, numbers, symbols

password_letters = [random.choice(alphabet) for i in range(random.randint(8, 10))]
password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)

password = "".join(password_list)
