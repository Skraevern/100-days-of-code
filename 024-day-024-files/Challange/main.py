# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names_list = file.readlines()
    # ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']

for name in names_list:
    stripped_name = name.strip()  # Removes \n
    edited_letter = starting_letter.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
        file.write(f"{edited_letter}")
