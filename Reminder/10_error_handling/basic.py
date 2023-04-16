# Error Handling
'''
Right now, getting an error, or 'exception', in your Python program means the entire program
will crash. You don't want this to happen in real-world programs. Instead, you want the program
to detect errors, handle them, and then continue to run.
'''

# Function without error handling
def spam(divideBy):
  return 42 / divideBy

print(spam(2))
print(spam(0)) # This will return 'ZeroDivisionError: division by zero
print(spam(3))

'''
Error can be handled with 'try' and 'except' statements. The code that could potentially have 
an error is put in a try clause. The program execution moves to the start of a following 'except'
clause if an error happens.
'''
def spam(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('Error: Invalid Argument.')
    
print(spam(2))
print(spam(0))
print(spam(3))