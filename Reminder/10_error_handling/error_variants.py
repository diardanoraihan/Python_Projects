'''
Error handling in Python.

Usually, when we create a program for the first time, the error can happen because of our mistakes.
But, once the program is done, the error can still happen because of the system, user input, or
things that are not expected.

Example:
- when we try to analyze big data, we want to convert all the numbers in a tabel into a float
    float("123.4") -> 123.4
    float("N/A") -> error

- Now you see the problem here. "N/A", "?", etc are common indicator of missing values.
  Instead of using if ... then ...., which would not be efficient, we can use a technique
  called error handling.

--------> Syntax Format
try:
# Try the following code. If this work, then fine.
except:
# If the codes in the try section does not work, we will enter this exception section.
# This block gets executed in the case of an error in the program

--------> Error Variants
- ValueError >> inappropriate argument value (of correct type).
    ex:
    keyWord = "Hello"
    print(int(keyWord))

- NameError >> Name not found globally

- IndexError >> Sequence index out of range.
    ex:
    li = [1,2,3]
    print(li[3])

- KeyboardInterrupt >> program interrupted by user

'''

# -------------------------- Basic Example -------------------------- #
try:
    print(int("Hello"))
    # This will trigger an error, specifically ValueError.
    # Hence, we will get to the exception section
except:
    print("Entered exception")

print("Pass exception 1")

# ------------------------ Passing the error  ---------------------- #
keyWord = "Hello"
try:
    print(int(keyWord))
except:
    # Indicating there is nothing you will do to handle the error, just moving on
    pass

print("Pass exception 2")

# --------------------- Catching the error ------------------------- #
try:
    print(int(keyWord))
# the following syntax will catch the error and print it as a string
except Exception as e:
    print(str(e))
print("Pass exception 3")

# print(int(keyWord))
# Notice if you print the code above, it will result in ValueError
# We can use ValueError as a key word to catch the error as follows:
try:
    print(int(keyWord))
except ValueError:
    print("Got a value error")
except: # You can also do other type of error handling
    print("Other type of exception")
finally: # Finally is everything you might do once the error is handled
    print("Finally we made it!")
    # The finally block get executed even if the except block does not
print("Pass exception 4")

# ----------------------------Raise an Error ---------------------- #
try:
    # Instead of having the computer saying you got an error,
    # now, you are the one saying you got an error
    raise NameError("error_1")
except ValueError:
    print("Got  value error")
except Exception as e:
    print("Got other type of error")
    print(str(e))
finally:
    print("Finally")
print("Pass exception 5")

