## No block scope in Python

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0] # Global

print(new_enemy) # "Skeleton"