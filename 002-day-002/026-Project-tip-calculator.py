print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
number_of_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

total_with_tip = (tip / 100 * total_bill) + total_bill
per_person = round(total_with_tip / number_of_people,2)

print("Each person should pay: $" + str(per_person))