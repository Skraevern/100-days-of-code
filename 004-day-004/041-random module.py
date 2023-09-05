import random
import my_module

random_integer = random.randint(1, 10)
random_float = random.random()

print(my_module.pi)
print(random_integer)
print(random_float)

random_float = random_float * 5 # Random float mellom 0 og 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")