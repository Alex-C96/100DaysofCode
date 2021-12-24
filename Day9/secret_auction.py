# Secret Auction Program
# Alexander Clarke
# 12/24/2021


# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep

# import art
from art import logo
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def take_bid():
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    bidder = {"name" : name, "bid" : bid}
    return bidder

def find_highest_bidder(all_bids):
    highest_bid = all_bids[0]['bid']
    highest_bidder_index = 0
    for i, bidder in enumerate(all_bids):
        if bidder['bid'] > highest_bid:
            highest_bid = bidder['bid']
            highest_bidder_index = i
    print(f"The highest bidder is {all_bids[highest_bidder_index]['name']} with a bid of {highest_bid}")

done_bidding = False
all_bids = []

print(logo)

while not done_bidding:
    all_bids.append(take_bid())
    done = input("Are there any other bidders? Please enter 'yes' or 'no': ")
    # check for more bidders
    if (done == 'no'):
        done_bidding = True
    clear()

find_highest_bidder(all_bids)

