'''
English Vocabulary Word List
Top 3000 US English Words #15 (126 Words)
http://www.manythings.org/vocabulary/lists/l/words.php?f=noll15
https://jrgraphix.net/r/Unicode/2500-257F
'''
import random
import time
from os import system, name
from Homescreen import HomeScreen
from Gamescreen import HangMan, Fields

# define our clear function
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def getWord():
	# Read the dictionary from the file vocab.txt
	with open('vocab.txt') as file:
		words = file.read()

	# Turn the words into a list of words
	words = words.split()

	# Pick a single word to play randomly
	numWord = random.randint(1,126)
	# print(words[numWord])
	return words[numWord]

gallow = ["",
          "   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
          "   \u2551      \u2502",
          "   \u2551      @",
          "   \u2551     \u2571\u257D\u2572",
		  "   \u2551     \u2571 \u2572",
          "   \u2551",
          "   \u2551",
          "\u2554\u2550\u2550\u2569\u2550\u2550\u2557"]


exit = False
back = False

while (exit!=True):

	# Initialiation
	hangman = HangMan()
	screen = HomeScreen()


	# Welcome the user
	clear()
	screen.titleShow()
	screen.menuShow(False, 0)
	userInput = int(input("Put your response here: "))

	# Start the game in 1-player mode
	if (userInput==1):
		word = getWord()
		fields = Fields(word)
		success = False
		while (hangman.status!=8) and (success == False):

			# ---------------- Game Screen ------------ #
			clear()
			screen.titleShow()
			screen.menuShow(True, 1)
			# ----------------------------------------- #
			hangman.Show()
			fields.Show()
			guess = input("\nYour response\t: ")
			hangman.addFalse(fields.updateField(guess))

			# Return True if the user successfully guessed all the letter
			success = fields.checkField()

		if success == True:
			# ---------------- Game Screen ------------ #
			clear()
			screen.titleShow()
			screen.menuShow(True, 1)
			# ----------------------------------------- #
			hangman.Show()
			print("You win!")
			print("Correct answer\t:", word)

		else:
			# ---------------- Game Screen ------------ #
			clear()
			screen.titleShow()
			screen.menuShow(True, 1)
			# ----------------------------------------- #
			hangman.Show()
			print("You lose!")
			print("Correct answer\t:", word)

		input("Press anything to continue . . .")

	# start the game in 2-player mode
	elif userInput ==2:
		# ---------------- Game Screen ------------ #
		clear()
		screen.titleShow()
		screen.menuShow(True, 2)
		# ----------------------------------------- #
		word = input("Player-1 to pick a word for Player-2 to guess: ")
		fields = Fields(word)
		success = False
		while (hangman.status!=8) and (success == False):

			# ---------------- Game Screen ------------ #
			clear()
			screen.titleShow()
			screen.menuShow(True, 2)
			# ----------------------------------------- #
			hangman.Show()
			fields.Show()
			guess = input("\nPlayer-2 input\t: ")
			hangman.addFalse(fields.updateField(guess))

			# Return True if the user successfully guessed all the letter
			success = fields.checkField()

		if success == True:
			# ---------------- Game Screen ------------ #
			clear()
			screen.titleShow()
			screen.menuShow(True, 2)
			# ----------------------------------------- #
			hangman.Show()
			print("Player-2 wins!")
			print("Correct answer\t:", word)

		else:
			# ---------------- Game Screen ------------ #
			clear()
			screen.titleShow()
			screen.menuShow(True, 2)
			# ----------------------------------------- #
			hangman.Show()
			print("Player-2 loses!")
			print("Correct answer\t:", word)

		input("Press anything to continue . . .")
	# exit the game
	elif userInput ==0:
		exit = True

print("See you!")







