'''
A function is like a miniprogram within a program.
- The purpose is to group code that gets executed multiple times.
- The code inside a function is executed when the function is called.

Remember that when you call the `print()` or `len()` function, you pass
them values, called "arguments", by typing them between parentheses.
You can also define your own functions that accepts arguments.
'''

def hello(name):
  print('Hello, ' + name)

hello('Diar')

test = 'test'

'''
Notice that the definition of `hello()` function has a parameter called
"name". A value being passed to a function in a function call is an argument.
Parameters are variables that contain arguments.

When a function is called with arguments, the arguments are stored in
the parameters. Consider the parameters as local variables that only valid
within the scope of the function.
'''