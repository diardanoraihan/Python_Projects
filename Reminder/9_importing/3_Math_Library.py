'''
Math library contains many useful functions
to do mathematical operations.

Some useful functions are:
- .sqrt
- .exp
- .factorial
- .sin/.cos
- .floor
- .ceil
'''

import math

# calculate the square root of a number
val  = 3
sqrtVal = math.sqrt(3)
print(sqrtVal)

# calculate the power of a number
expVal = math.exp(3)
print(expVal)

# calculate the factorial of a number
factVal = math.factorial(5)
print(factVal)

# trigonometric function
sinVal = math.sin(val)
print(sinVal)

# flooring the number by rounding it down to the lowest int value
floorVal = math.floor(val+0.64)
print(floorVal) # 3

# Ceiling the number by rounding it up to the highest int value
# Pretty much the opposite of flooring
ceilingVal = math.ceil(val+0.64)
print(ceilingVal) #4

