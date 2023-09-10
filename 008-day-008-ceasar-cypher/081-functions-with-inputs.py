# simple function
def greet():
    print("I")
    print("like")
    print("pizza!")

greet()

# input function
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")

greet_with_name("Lars")

# function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is the weather like in {location}?")

greet_with("Lars", "Finland")

# Keyword arguments
def my_function(a, b, c):
    print(a)
    print(b)
    print(c)

my_function(a=1, b=2, c=3) # 1 2 3
my_function(c=1, b= 2, a=3) # 3 2 1
greet_with(location="Oslo", name=("Lars"))