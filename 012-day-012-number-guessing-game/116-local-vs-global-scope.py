enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}") # 2

increase_enemies()
print(f"Enemies outside function: {enemies}") # 1

enemies2 = 1

def increase_enemies2():
    global enemies2
    enemies2 = 2
    print(f"Enemies2 inside function: {enemies2}") # 2

increase_enemies()
print(f"Enemies2 outside function: {enemies2}") # 2

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength) # 2

drink_potion()
# print(potion_strength) Not defined

# Global Scope     Availible everywhere in code
player_health = 10

def drink_potion2():
    def game():
        print("ja")
    potion_strength = 2
    print(player_health) # 10

drink_potion2()
# game() # Error
