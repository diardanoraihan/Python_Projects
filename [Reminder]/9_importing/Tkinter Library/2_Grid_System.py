'''
Grid's System

We can position the widget using Tkinter grid system. Think of it as rows and columns of the windows.

row number = 0 ... N
col number = 0 ... N
'''

# Import all functions inside tkinter library
from tkinter import *

# Root widget
root = Tk()

#---------------------------GUI: Positioning with Tkinter Grid's System ------------

# Create the label widgets
myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='My name is Diardano Raihan')

# Showing it onto the screen with grid system
myLabel1.grid(row=0, column = 0)
myLabel2.grid(row=1, column = 1)

# Execute the GUI
root.mainloop()