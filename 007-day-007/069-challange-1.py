import random

word_list = ["ardvark", "baboon", "camel"]
solution_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()
if len(guess) == 1:
    for i in range(0, len(solution_word)):
        if guess == solution_word[i]:
            print("Right")
        else:
            print("Wrong") 
else:
    print("Game over. Please enter just one letter.")
