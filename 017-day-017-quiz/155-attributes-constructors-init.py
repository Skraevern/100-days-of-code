class User:
    def __init__(self):
        print("User is being created")

class Car:
    def __init__(self, seats):
        self.seats = seats

class UserClassTwo:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User() # User is being created
user_1.id = "001"
user_1.username = "angela"

user_2 = User() # User is being created

print (user_1.id) # 001
print (user_1.username) # angela

my_car = Car(5)
print(my_car.seats) # 5

user_3 = UserClassTwo(549, "Lars")
print(user_3.id) # 549
print(user_3.username) # Lars
print(user_3.followers) # 0

