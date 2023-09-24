file = open("my_file.txt")
contents = file.read()
print(contents)  # Hello my name is Angela.
file.close()  # Viktig!

with open("my_file.txt") as file:  # Trenger ikke close
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:  # Write
    file.write("New text.")

with open("my_file.txt", mode="a") as file:  # Append
    file.write("\nNew new text.")

# New text.
# New new text

with open("new_file.txt", mode="w") as file:  # new_file does not exist. Gets created
    file.write("New file")
