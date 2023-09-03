num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters") #TypeError: can only concatenate str (not "int") to str
print(type(num_char)) # <class 'int'>
print("Your name has " + str(num_char) + " characters")

a = float(123)
print(type(a)) # <class 'float'>

print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100