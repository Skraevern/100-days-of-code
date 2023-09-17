from prettytable import PrettyTable

table = PrettyTable()
print(table)
# ++
# ||
# ++
# ++

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
print(table)
# +--------------+
# | Pokemon Name |
# +--------------+
# |   Pikachu    |
# |   Squirtle   |
# |  Charmander  |
# +--------------+

table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
# +--------------+----------+
# | Pokemon Name |   Type   |
# +--------------+----------+
# |   Pikachu    | Electric |
# |   Squirtle   |  Water   |
# |  Charmander  |   Fire   |
# +--------------+----------+

print(table.align) # {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
table.align = "l"
print(table)
# +--------------+----------+
# | Pokemon Name | Type     |
# +--------------+----------+
# | Pikachu      | Electric |
# | Squirtle     | Water    |
# | Charmander   | Fire     |
# +--------------+----------+
print(table.align) # {'base_align_value': 'c', 'Pokemon Name': 'l', 'Type': 'l'}

