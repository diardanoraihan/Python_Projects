import random as rd

user_guess = input("Heads or Tails: ")
random_integer = rd.randint(0, 1)
if random_integer == 1:
    app_answer = "Heads"
else:
    app_answer = "Tails"

test = {"1": 1234, "2": 2345, "3": 4567}

if user_guess == app_answer:
    print("You guessed correctly!")
else:
    print("You were wrong!")
    
