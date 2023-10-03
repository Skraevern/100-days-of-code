# File not found
# with open("a_file.txt") as file:
# file.read()
#  No such file or directory: 'a_file.txt'

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]
# 'non_existent_key'

# index error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
# IndexError: list index out of range

# TypeError
# text = "abc"
# print(text + 5)
# TypeError: can only concatenate str (not "int") to str


# Exceptions
# try:          Something that might cause an exception
# except:       Do this if there was an exception
# else:         Do this if there were no exceptions
# finally:      Do this no matter what happens

try:
    file = open("./a_file.txt")
    a_dict = {"Key": "Value"}
    print(a_dict["Valueee"])
except FileNotFoundError:
    file = open("./a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print("Key error")
    print(f"The key {error_message} does not exist")
else:  # If noe errors where found in try. What "else" do you want to do?
    content = file.read()
    print(content)
finally:  # do no matter what happens
    file.close()
    print("File was closed")
