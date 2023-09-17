class Car:
    def __init__(self) -> None:
        self.seats = 5

    def enter_race_mode(self):
        self.seats = 2

class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

        


new_car = Car()
print(new_car.seats) # 5
new_car.enter_race_mode()
print(new_car.seats) # 2

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers) # 0
print(user_1.following) # 1
print(user_2.followers) # 1
print(user_2.following) # 0