import random as rd
from os import system, name # Optional
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
============= 
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
============= 
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
============= 
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
============= 
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
============= 
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
============= 
''', '''
  +---+
  |   |
      |
      |
      |
      |
============= 
''']

# Optional
# define our clear function
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

word_list = ['book', 'pencil', 'pen', 'paper']
# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = rd.choice(word_list)
print(chosen_word)

# TODO-2: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = []
for letter in chosen_word:
  placeholder.append("_")
print(' '.join(placeholder))

# TODO-3: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Note: Use a while loop to let the user guess again.
lives = 6
print(stages[lives])
game_over = False
correct_letters = []
while not game_over:
  guess = input('Guess a letter: ').lower()
  display = []

# TODO-4: Create a "display" that puts the guess letter in the right position. 
# Note: Make sure the loop can keep the previous correct guess.

  for letter in chosen_word:
    if letter == guess:
      display.append(letter)
      correct_letters.append(guess)
    elif letter in correct_letters:
      display.append(letter)
    else: 
      display.append("_")
      
  clear()
  
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      game_over = True
      print("You Lose!")
  
  if "_" not in display:
    game_over = True
    print("You Win!")
  
  print(' '.join(display))
  print(stages[lives])