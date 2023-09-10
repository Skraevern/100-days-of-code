import random
import stages
import hangman_words

word_list = hangman_words.words
solution_word = random.choice(word_list)
display = []
end_game = False
lives = 6
for letter in solution_word:
        display.append("_")

def print_game():
    print(stages.stages[lives])
    print(f"{' '.join(display)}") #Join all the elements in the list and turn it into a String.
     
print(solution_word)
print_game()

while end_game == False:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
        for i in range(0, len(solution_word)): #checks if guessed letter is in word
            if guess == solution_word[i]:
                display[i] = guess
        if guess not in solution_word:
             lives -= 1

        print_game()

        if "_" not in display:
             end_game = True
             print("You win!")
        if lives == 0:
             end_game = True
             print("You loose...")
    else:
        print("Please enter one letter.")
