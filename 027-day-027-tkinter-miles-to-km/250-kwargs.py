def calculate(**kwargs):
    print(kwargs)  # {'add': 2, 'multiply': 5}
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(key)  # add # multiply
        print(value)  # 2 # 5
    print(kwargs["add"])  # 2


calculate(add=2, multiply=5)
# add = key
# 2 = value
# multiply = key
# 5 = value

print("")


def calculate2(num, **kwargs):
    num += kwargs["add"]
    print(num)  # 4 + 2 = 6
    num *= kwargs["multiply"]
    print(num)  # 6 * 5 = 30


calculate2(4, add=2, multiply=5)

print("")


class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GTR")
print(my_car.make)  # Nissan
print(my_car.model)  # GTR
# my_car2 = Car(make="Nissan") # KeyError: 'model'


class Car2:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car2 = Car2(make="Nissan")
print(my_car2.make)  # Nissan
print(my_car2.model)  # None
