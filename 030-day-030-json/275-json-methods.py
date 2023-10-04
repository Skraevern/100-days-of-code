import json

# Write
# json.dump()

# Read
# json.load()

# Update
# json.update()

website = "www.vg.no"
email = "mail@mail.com"
password = "1234"

with open("passwords.json", mode="r") as file:
    # Reading old data
    data = json.load(file)
    # Updating old data
    new_data = {website: {"email": email, "password": password}}
    data.update(new_data)
with open("passwords.json", "w") as file:
    # Saving updated data
    json.dump(data, file, indent=4)
