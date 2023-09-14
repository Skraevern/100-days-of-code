import art
import random
import os

def print_logo():
    os.system("cls||clear")
    print(art.logo)

def reset_hands():
    """Resets cars and scores"""
    global player_cards, dealer_cards, player_score, dealer_score
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0

def deal_start_cards():
    """Deals out to cards to player and dealer"""
    global player_cards, dealer_cards
    for i in range(0, 2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())

def calculate_scores(card_list):
    """Calculates total in card list"""
    score = 0
    for i in  range(0, len(card_list)):
        score += card_list[i]
    if score > 21:
        if 11 in card_list:
            score -= 10
    return score

def check_winner():
    global player_score, dealer_score
    print_logo()
    if player_score == 21:
        print("                         BlackJack!")
    if player_score > 21:
        print_hands()
        print("                        You bust. Dealer win.")
    else:
        while dealer_score < 17 or dealer_score < player_score:
            dealer_cards.append(draw_card())
            dealer_score = calculate_scores(dealer_cards)
        
        if dealer_score == 21:
            print("                    Dealer has BlackJack!")

        print_hands()
        if dealer_score > 21:
            print("                    Dealer bust. You win!")
        elif player_score == dealer_score:
            print("                    Draw")
        elif player_score > dealer_score:
            print("                    You win!")
        else:
            print("                    Dealer wins..")

def print_hands():
    print(f'            Your final hand: {player_cards}, final score: {player_score}')
    print(f"            Dealers final hand: {dealer_cards}, final score: {dealer_score}")

def draw_card():
    card = random.choice(cards)
    return card

def play_blackjack():
    global want_to_play, player_cards, dealer_cards, player_score, dealer_score, cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while want_to_play == "y":
        print_logo()
        if len(player_cards) == 0:
            deal_start_cards()

        player_score = calculate_scores(player_cards)
        dealer_score = calculate_scores(dealer_cards)

        print(f"            Your cards: {player_cards}. Current score {player_score}")
        print(f"            Dealers first card: {dealer_cards[0]}")
        print(f"            Dealer cards: {dealer_cards}. Current score {dealer_score}")

        if player_score > 20:
            want_to_play = "n"
        else:
            another_card = input('Type "y" to draw another card, type "n" to pass: ').lower()
            if another_card == "y":
                player_cards.append(draw_card())
                calculate_scores(player_cards)
            else:
                want_to_play = "n"
    
    check_winner()

    want_to_play = input('Do you want to play a game of blackjack? Type "y" or "n": ').lower()
    if want_to_play == "y":
        reset_hands()
        play_blackjack()
        
os.system("cls||clear")
want_to_play = input('Do you want to play a game of blackjack? Type "y" or "n": ').lower()

if want_to_play == "y":
    reset_hands()
    play_blackjack()