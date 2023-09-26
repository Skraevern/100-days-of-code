# FOR loop
numbers = [1, 2, 3]
new_list = []
for num in numbers:
    new_list.append(num + 1)
print(new_list)  # [2, 3, 4]

# list comprehension

# new_list = [new_item for item in list]
new_list = [num + 1 for num in numbers]
print(new_list)  # [2, 3, 4]

name = "Angela"
name_list = [letter for letter in name]
print(name_list)  # ['A', 'n', 'g', 'e', 'l', 'a']


# new_list = [new_item for item in range]
range_list = [num * 2 for num in range(1, 5)]
print(range_list)  # [2, 4, 6, 8]

# new_list [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names_list = [name for name in names if len(name) == 4]
print(short_names_list)  # ['Alex', 'Beth', 'Dave']

upper_case = [name.upper() for name in names if len(name) > 5]
print(upper_case)  # ['CAROLINE', 'ELEANOR', 'FREDDIE']
