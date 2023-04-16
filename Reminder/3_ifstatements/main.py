"""
Title:
Homework Assignment #3: "if" statement

Details:
Create a function that accepts 3 parameters and checks for equality
between any two of them.

Your function should return True if 2 or more of the parameters are equal,
and false is none of them are equal to any of the others.
"""

def funct(param1, param2, param3):
    if int(param1) == int(param2):
        return True
    elif int(param1) == int(param3):
        return True
    elif int(param2) == int(param3):
        return True
    else:
        return False

result = funct(6,5,'5')
print(result)
