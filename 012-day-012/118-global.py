# Modifying global scope

enemies = 2
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}") # 3

increase_enemies()
print(f"Enemies outside function: {enemies}") # 3