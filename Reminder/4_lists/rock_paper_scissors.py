import random as rd

rock_paper_scissors = ['Rock', 'Paper', 'Scissors']

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
if user_input < len(rock_paper_scissors):
  user_choice = rock_paper_scissors[user_input]
  computer_choice = rd.choice(rock_paper_scissors)
  print(f'You Chose:\n{user_choice}')
  print(f'Computer chose:\n{computer_choice}')
  if user_choice == computer_choice:
    print('You draw')
  elif user_choice == 'Rock':
    if computer_choice == 'Paper':
      print('You Lose')
    else:
      print('You Win')
  elif user_choice == 'Paper':
    if computer_choice == 'Scissors':
      print('You Lose')
    else:
      print('You Win')
  elif user_choice == 'Scissors':
    if computer_choice == 'Rock':
      print('You Lose')
    else:
      print('You Win')
else:
  print('You typed an invalid number. You Lose!')