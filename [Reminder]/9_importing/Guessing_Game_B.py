from random import random

upper = 100
lower = 0
guess = int((upper+lower)/2) # 50 as the first guess

print("Think of a number between 1 and 100")
menu = ['q', 'Q', 'l', 'L', 'h', 'H', 'y', 'Y']
attempt = 0

while (True):
    attempt+=1
    print("I guessed it's {}, am I right?".format(guess))
    print("q/Q: quit, l/L: too low, h/H: too high, y/Y: yes")
    userInput = input("Your input: ")

    # User input validation
    while (userInput not in menu):
        print("I didn't recognize your input")
        userInput = input("Your input: ")

    # User input classification
    if (userInput in menu[:2]): # 'q'/'Q'
        print("You quit, bye!")
        break
    elif (userInput in menu[2:4]): # 'l'/'L'
        lower = guess
    elif (userInput in menu[4:6]): # 'h'/'H'
        upper = guess
    elif (userInput in menu[6:8]): # 'y'/'Y'
        print("I guessed it in {} attempts.".format(attempt))
        break
    guess = int((upper+lower)/2)
