import os
import art

bidding_list = []
keep_bidding = True
winner = ""
winning_bid = 0

def bidders():
    """Asks for input and saves name and 
    bid amount as dictionary in bidding_list"""
    bidder = {}
    bidder["name"] = input("What is your name? ")
    bidder["bid"] = int(input("What's tour bid: $"))
    bidding_list.append(bidder)

def check_winner():
    """Checks which bid is highest and saves it in variables"""
    global winning_bid, winner
    for i in range(0, len(bidding_list)):
        if int(bidding_list[i]["bid"]) > int(winning_bid):
            winning_bid = bidding_list[i]["bid"]
            winner = bidding_list[i]["name"]


os.system("cls||clear")
print(art.logo)
print("Welcome to the secret auction program.")

while keep_bidding == True:
    bidders()
    more_bidders = input('Are there any other bidders? Type "yes" or "no": ').lower()
    os.system("cls||clear")
    if more_bidders == "no":
        keep_bidding = False

check_winner()

print(f"The winner is {winner} with a bid of ${winning_bid}")




    


