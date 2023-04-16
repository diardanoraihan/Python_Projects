'''
In tkinter, everything is a widget.
The first thing you need to create is the root widget.

Root widget is like the windows of your GUI.

There are 2 steps in tkinter:
1. Define / create a thing
2. Put the thing up on the screen

Finally, you need to create an infinite loop to keep your program running
'''

# Import all functions inside tkinter library
from tkinter import *

# Root widget
root = Tk()

# -----------------------------GUI: "Hello World" Introduction ---------------------

# Create a label widget
myLabel = Label(root, text='Hello World')
# Showing it onto the screen
myLabel.pack()
# Execute the GUI
root.mainloop()