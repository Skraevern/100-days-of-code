import random
import hangman_art
import hangman_words

solution_word = random.choice(hangman_words.words)
already_guessed = []
display = []
end_game = False
lives = 6
for letter in solution_word:
    display.append("_")


def print_game():
    print(hangman_art.stages[lives])
    print(
        f"{' '.join(display)}"
    )  # Join all the elements in the list and turn it into a String.


print(hangman_art.logo)
# print(f"------   Solution word is {solution_word}   ------")
print_game()

while end_game == False:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
        if guess in already_guessed:
            print(f"You have already guessed {guess}. Try another letter.")
        else:
            already_guessed.append(guess)
            for i in range(0, len(solution_word)):  # in solution_word?
                if guess == solution_word[i]:
                    display[i] = guess  # replace "_" with guess
            if guess not in solution_word:
                lives -= 1

        print_game()

        if "_" not in display:
            end_game = True
            print("You win!")
        if lives == 0:
            end_game = True
            print(f'You loose... The word was "{solution_word}"')
    else:
        print("Please enter one letter.")
