import random
from replit import clear
from art import logo

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0,13)]

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  #return sum(cards) 
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "You lose!"
  elif user_score == 0:
    return "You Win!"
  elif user_score > 21:
    return "You lose!"
  elif computer_score>21:
    return "You Win!"
  elif user_score > computer_score:
    return "You Win!"
  else:
    return "You Lose!"
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print(user_cards)
  print(computer_cards)
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'Your cards {user_cards}, current score: {user_score}')
    print(f'Computer first card: {computer_cards[0]}')
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over = True
    else :
      should_continue = input("Type 'y' to get another card, type n to pass:")
      if should_continue == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  
        
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0  and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand is {user_cards} and score is {user_score}")
  print(f"Computer final hand is {computer_cards} and score is {computer_score}")
  print(compare(user_score, computer_score))
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of BlackJack?Type 'y' or 'n':") == 'y':
  clear()
  play_game()