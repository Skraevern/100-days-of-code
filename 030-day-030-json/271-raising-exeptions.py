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
    # raise KeyError("This is an error that i made up")  # Gives KeyError
    pass


height_in_meters = 45
weight_in_kg = 70

if height_in_meters > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = float(weight_in_kg / height_in_meters**2)
print(bmi)  # 0.0345679012345679
