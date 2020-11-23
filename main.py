from replit import clear
from art import logo
stop_bid=False
all_bids={}
while not stop_bid:
  print(logo)
  bid_holder=input("What's your name? ")
  bid_amount=input("What's your bid? $")
  all_bids[bid_holder]=bid_amount
  close_auction=input("Stop bidding? type 'yes' or 'no': ").lower()
  if(close_auction=='yes'):
    stop_bid=True
    clear()
    print(logo)
    highest_bid=max(all_bids.values())
    for k in all_bids.keys():
      if(all_bids[k]==highest_bid):
        print(f'{k} is the Winner with highest amount ${highest_bid}')
  elif(close_auction=='no'):
    clear()

