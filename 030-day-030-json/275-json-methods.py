import json

# Write
# json.dump()

# Read
# json.load()

# Update
# json.update()

website = "www.ta.no"
email = "mail@mail.com"
password = "1234"
new_data = {website: {"email": email, "password": password}}

try:
    with open("passwords.json", mode="r") as file:
        # Reading old data
        data = json.load(file)
        # Updating old data
        data.update(new_data)
    with open("passwords.json", "w") as file:
        # Saving updated data
        json.dump(data, file, indent=4)
except FileNotFoundError:  # if no file. Write new.
    with open("passwords.json", mode="w") as file:
        json.dump(new_data, file, indent=4)
