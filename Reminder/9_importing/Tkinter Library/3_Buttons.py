# Import all functions inside tkinter library
from tkinter import *

# --------------------------GUI: Creating Buttons-----------------------
# myButton = Button(root, text="Click Me!", state=DISABLED)
root = Tk()
# Create an actionable function after clicking the button
def myClick():
    myButton = Button(root, text='You just clicked a button!!')
    myButton.pack()

# make the button size wider in x and y axis by padding it and put color on it
myButton = Button(root, text='Click Me', padx = 50, pady = 50,
                  command=myClick, fg='white', bg='blue')
myButton.pack()
root.mainloop()