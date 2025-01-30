from art import logo


def find_highest_bid(dictionary):
    winner = ""
    highest_bid = 0

    for user in dictionary:
        amount = dictionary[user]
        if amount > highest_bid:
            highest_bid = amount
            winner = user

    print(f"The winner is {winner} with bid of ${highest_bid}")


print(logo)
bid_data = {}
auction_will_continue = True

while auction_will_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bid_data[name] = bid

    if continue_auction == 'no':
        auction_will_continue = False
        find_highest_bid(bid_data)
    elif continue_auction == 'yes':
        print("\n" * 20)
