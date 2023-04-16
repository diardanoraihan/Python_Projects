'''
Importing allows you to use function that someone has built
to your needs.
Normally, these functions are stored inside a library.
Some functions we explore in random library:
- randint
- random
- uniform
- choice
- shuffle
'''

import random as r
from random import randint

r.seed(1) # to generate the same randomness everytime the function gets called
randInt = randint(0, 10) # start <= random_number <= end
print(randInt)

# Return the next random floating point number in the range [0.0, 1.0).
randFloat = r.random()
print(randFloat)

# Return a random floating point number N
# such that a <= N <= b for a <= b and b <= N <= a for b < a.
randUniform = r.uniform(1,110)
print(randUniform)

simpleList = [1,3,5,7,9]
pickElement = r.choice(simpleList)
print(pickElement)

print(simpleList) # [1, 3, 5, 7, 9]
r.shuffle(simpleList) # shuffle the sequence of mutable list
print(simpleList) # [5, 7, 9, 1, 3]