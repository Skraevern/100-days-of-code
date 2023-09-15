import os
import art
import game_data
import random

def higher_lower_game():
    first_guess = True
    continue_game = True
    score = 0
    random_b = random.randint(0, len(game_data.DATA) - 1)
    while continue_game:
        random_a = random_b
        random_b = random.randint(0, len(game_data.DATA) - 1)
        while random_a == random_b:
            random_b = random.randint(0, len(game_data.DATA) - 1)
        follower_count_a = game_data.DATA[random_a]["follower_count"]
        follower_count_b = game_data.DATA[random_b]["follower_count"]
        name_a = game_data.DATA[random_a]["name"]
        name_b = game_data.DATA[random_b]["name"]
        description_a = game_data.DATA[random_a]["description"]
        description_b = game_data.DATA[random_b]["description"]
        country_a = game_data.DATA[random_a]["country"]
        country_b = game_data.DATA[random_b]["country"]
        
        os.system("cls||clear")
        print(art.LOGO)
        if not first_guess:
            print(last_guess)
        print(f'Compare A: {name_a}, a {description_a}, from {country_a}')
        print(art.VS)
        print(f'Against B: {name_b}, a {description_b}, from {country_b}')
        #print(f"A: {follower_count_a} B: {follower_count_b}")
        guess = input('Who has more followers? Type "A" or "B": ').upper()
        first_guess = False
        
        if (follower_count_a > follower_count_b and guess == "A") or (follower_count_a < follower_count_b and guess == "B"):
            score += 1
            last_guess = f'Correct. {name_a}: {follower_count_a} vs {name_b}: {follower_count_b}.\nScore: {score}'
        elif follower_count_a == follower_count_b:
            last_guess = f'Draw! {name_a}: {follower_count_a} vs {name_b}: {follower_count_b}.\nScore: {score}'
        else:
            last_guess = f'Sorry thats wrong. {name_a}: {follower_count_a} vs {name_b}: {follower_count_b}.\nFinal score: {score}'
            continue_game = False

    os.system("cls||clear")
    print(last_guess)

    
    
higher_lower_game()