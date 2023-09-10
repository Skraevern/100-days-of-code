import random
import hangman_art
import hangman_words
import os  # for clearing terminal

guess = ""
solution_word = random.choice(hangman_words.words)
already_guessed_list = []
already_guessed = False
display = []
end_game = False
lives = 6
for letter in solution_word:
    display.append("_")


def print_game():
    global already_guessed
    global guess
    os.system("cls||clear")  # Clear terminal
    # print(f"------   Solution word is {solution_word}   ------")
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    print(
        f"{' '.join(display)}"
    )  # Join all the elements in the list and turn it into a String.
    if already_guessed == True:
        print(f"You have already guessed {guess}. Try another letter.")
    already_guessed = False


while end_game == False:
    print_game()
    guess = input("Guess a letter: ").lower()

    if len(guess) == 1:
        if guess in already_guessed_list:
            already_guessed = True
        else:
            already_guessed_list.append(guess)
            for i in range(0, len(solution_word)):  # in solution_word?
                if guess == solution_word[i]:
                    display[i] = guess  # replace "_" with guess
            if guess not in solution_word:
                lives -= 1

        if "_" not in display:
            end_game = True
            print("You win!")
        if lives == 0:
            end_game = True
            print(f'You loose... The word was "{solution_word}"')
    else:
        print("Please enter one letter.")
