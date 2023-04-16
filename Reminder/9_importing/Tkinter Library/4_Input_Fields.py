'''
Input Fields
Several class needs to be included:

1. Entry()
- .get()
- .pack()
- .insert()

2. Button()

'''
#-------------------------GUI: Creating Input Fields---------------------------
# Import all functions inside tkinter library
from tkinter import *
root = Tk()
# Create a widget of input box
entry = Entry(root, width = 50, bg='red', fg='white', borderwidth = 5)
entry.pack()
entry.insert(0, "Enter your name:")

# Create an actionable function after clicking the button
def myClick():
    hello = "Hello " + entry.get() + "!"
    myButton = Button(root, text=hello)
    myButton.pack()

# make the button size wider in x and y axis by padding it and put color on it
myButton = Button(root, text='Enter your name', padx = 50, pady = 50,
                  command=myClick, fg='white', bg='blue')
myButton.pack()
root.mainloop()