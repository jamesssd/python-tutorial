# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bids = {}
bidding_finished = False

def find_highest(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount= bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")       
     
while not bidding_finished:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    bids[name] = amount
    should_continue = input("Are they any bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest(bids)
    elif should_continue == 'yes':
        #needs to find a clear function clear()
        print("clear")