programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expoected.",
    "Function": "A piece of code that you can easily call over and over again",
}

# Retrieving from dictioanry
print(programming_dictionary["Bug"])

# adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over."
print(programming_dictionary)

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}

# edit an item i dictionary 
programming_dictionary["Bug"] = "A moth in your computer"

# Loop trough a dictionary
for key in programming_dictionary:
    print(key)                        # Bug Function Loop
    print(programming_dictionary[key])

