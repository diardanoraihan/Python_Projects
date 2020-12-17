'''
Computer decides to pick one random integer value between 0 and 100
and our task is to guess this number correctly.
'''

from random import randint

# randVal = a <= N <= b
randVal = randint(0,100)
attempts = 0

# while (true==true)
while (True):
    attempts+=1
    guess = int(input("Please enter your guess: "))
    if (guess==randVal):
        break
    elif (guess < randVal):
        print('Your guess was too low.')
    else:
        print('Your guess was too high.')

print('You guessed correctly with: {} in {} attempts'.format(guess, attempts))





