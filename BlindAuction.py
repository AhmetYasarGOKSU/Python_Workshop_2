import os 
def clear():
    os.system("cls")
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to Blind Auction.")
bid_dict = {}
while True:
    name = input("What is your name: ")
    bid = input("What is your bid: ")
    bid_dict[name] = bid
    other_bids = input("Are there other bids? Type y or n : ").lower()
    if other_bids == "y":
        clear()
        continue
    else:
        break
highest_bidder = []
highest_bidder.append(list(bid_dict)[0])
highest_bid = bid_dict[list(bid_dict)[0]]
for i in bid_dict:
    if bid_dict[i] > highest_bid:
        highest_bid = bid_dict[i]
        highest_bidder[0] = i 
    elif bid_dict[i] == highest_bid:
        highest_bidder.append(i)
        if highest_bidder[0] == highest_bidder[1]:
            highest_bidder.pop(1)
print(f"Blind Auction winner is {highest_bidder} with {highest_bid}$")        

