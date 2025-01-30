from art import logo

print(logo)
bid_data = {}

auction_will_continue = True

while auction_will_continue:
  # TODO-1: Ask the user for input
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  continue_auction = input("Are there any other bidders? Type 'yes' or 'no': ")
  # TODO-2: Save data into dictionary {name: price}
  bid_data[name] = bid
  # TODO-3: Whether if new bids need to be added
  if continue_auction == 'no':
    auction_will_continue = False

  print("\n" * 25)
# TODO-4: Compare bids in dictionary
max_key = max(bid_data, key=bid_data.get)
# print(bid_data)
print(f"The winner is {max_key} with bid of ${bid_data[max_key]}")

# my_dict = {'a': 10, 'b': 25, 'c': 1005, 'Jasper': 2000}
#
# max_key = max(my_dict, key=my_dict.get)
# print(max_key)
