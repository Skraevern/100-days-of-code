#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

import random

word_list = ["ardvark", "baboon", "camel"]
solution_word = random.choice(word_list)
display = []
end_game = False
for letter in solution_word:
        display.append("_")

print(solution_word)
print(display)

while end_game == False:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
        for i in range(0, len(solution_word)): #checks if guessed letter is in word
            if guess == solution_word[i]:
                display[i] = guess
        print(display)

        if "_" not in display:
             end_game = True
    else:
        print("Please enter one letter.")
print("Woop")
print(display)