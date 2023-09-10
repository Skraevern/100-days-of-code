# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1): # 2, 3, 4, 5, 6
        if number % i == 0:
           is_prime = False
    if is_prime == True:
       print("It's a prime number.")
    else:
       print("It's not a prime number.")
   
# number = 7
# 7 / 2 = 3,5 
# 7 / 3 = 2,33
# 7 / 4 = 1,75
# 7 / 5 = 1,4
# 7 / 6 = 1,17
# Altså kun delbart i hele tall med seg seg selv(7) og 1 = Primtall

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)