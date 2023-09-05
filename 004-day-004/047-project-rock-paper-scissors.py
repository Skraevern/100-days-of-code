rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("\nLets play rock paper scissors!")
import random

player_choice = input('\nType "Rock" "Paper" or "Scissors"\n').lower()


if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
    print("Your choice:")
    if player_choice == "rock":
        print(rock)
    if player_choice == "paper":
        print(paper)
    if player_choice == "scissors":
        print(scissors)
    
    computer_number = random.randint(0, 2)
    print("Computer choice:")
    if computer_number == 0:
        computer_choice = "rock"
        print(rock)
    if computer_number == 1:
        computer_choice = "paper"
        print(paper)
    if computer_number == 2:
        computer_choice = "scissors"
        print(scissors)
    
    print_txt = f'You picked "{player_choice}" and the computer picked "{computer_choice}". '
    player_wins = "You win!"
    computer_wins = "Computer wins..."

    if player_choice == computer_choice:
        print(print_txt + "Its a draw!")
    
    if player_choice == "rock" and computer_choice == "paper":
        print(print_txt + computer_wins)
    if player_choice == "rock" and computer_choice == "scissors":
        print(print_txt + player_wins)
    
    if player_choice == "paper" and computer_choice == "scissors":
        print(print_txt + computer_wins)
    if player_choice == "paper" and computer_choice == "rock":
        print(print_txt + player_wins)

    if player_choice == "scissors" and computer_choice == "rock":
        print(print_txt + computer_wins)
    if player_choice == "scissors" and computer_choice == "paper":
        print(print_txt + player_wins)


else:
    print("Game over. Please enter correct choice.")
