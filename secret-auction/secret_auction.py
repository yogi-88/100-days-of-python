import os
import sys
from art import logo
print(logo)

bid_records = {}
should_repeat = True

def highest_bidder_finder(bid_records):

    highest_bid = 0
    winner = ""
    for bidder in bid_records:
        bid_amount = bid_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of ${bid_amount}")


while should_repeat:
    user_name = input("What is your name?:  ")
    bid_price = int(input("What is your bid price?: $ "))
    bid_records[user_name] = bid_price

    restart_bidding = input("if there are other users who want to bid? Type 'yes' or 'no':   ")
    if restart_bidding == "no":
        should_repeat = False
        highest_bidder_finder(bid_records)
    elif restart_bidding == "yes":
        os.system('cls')



