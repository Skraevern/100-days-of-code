class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("inhale")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Under water")

    def swim(self):
        print("swum")


nemo = Fish()
nemo.swim()  # swum
nemo.breathe()  # inhale # under water
print(nemo.num_eyes)  # 2
