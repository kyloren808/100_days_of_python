import random as rnd
from art import logo

def deal_card():
  """Returns a random card from the card list (deck)"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = rnd.choice(cards)
  return card

def calculate_score(cards):
  """Takes a list of cards and returns the calculated score"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(u_score, c_score):
  if u_score == c_score:
    return "Draw 😐"
  elif c_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif u_score == 0:
    return "Win with Blackjack 😎"
  elif u_score > 21:
    return "You went over. You lose 😭"
  elif c_score > 21:
    return "Opponent went over. You win 😁"
  elif u_score > c_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)
  player_cards = []
  computer_cards = []
  user_score = -1
  computer_score = -1
  is_game_over = False

  for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}, current score {user_score}")
    print(f"Computer first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      deal_user_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if deal_user_card == 'y':
        player_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {player_cards}, final score: {user_score}")
  print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  print("\n" * 20)

  play_game()
