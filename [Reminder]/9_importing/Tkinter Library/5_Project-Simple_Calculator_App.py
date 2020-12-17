# Import all functions inside tkinter library
from tkinter import *
root = Tk()
root.title("Simple Calculator")

# Build an entry for the user input
entry = Entry(root, width = 40, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady=10)


# Define the command functions for each button

def button_click(number):
    # entry.delete(0, END)
    current = entry.get() # get the current value in the field
    entry.delete(0, END)  # Delete text from FIRST to LAST (0 here means from first)
                          # (END here is a literal constant for 'end' LAST)
    entry.insert(0, str(current)+ str(number)) # update the field

def button_DOT(str):
    current = entry.get()
    if len(current)==0:
        entry.insert(0, '.')
    else:
        entry.delete(0, END)
        current = current+'.'
        entry.insert(0, current)
    
def button_ZEROS():
    current = entry.get()
    if len(current)==0:
        entry.insert(0, str(1000))
    else:
        entry.delete(0, END)
        current = float(current)
        current = current*1000
        entry.insert(0, str(current))
        
def button_AC():
    entry.delete(0, END)
        
def button_ADD():
    first_number = entry.get()
    global f_num
    global math
    math = '+'
    f_num = float(first_number)
    entry.delete(0, END)
    
def button_SUBSTRACT():
    first_number = entry.get()
    global f_num
    global math
    math = '-'
    f_num = float(first_number)
    entry.delete(0, END)

def button_MULTIPLY():
    first_number = entry.get()
    global f_num
    global math
    math = '*'
    f_num = float(first_number)
    entry.delete(0, END)

def button_DIVIDE():
    first_number = entry.get()
    global f_num
    global math
    math = '/'
    f_num = float(first_number)
    entry.delete(0, END)

def button_EQUAL():
    second_number = entry.get()
    entry.delete(0, END)
    s_num = float(second_number)
    if math=='+':
        answer = f_num + s_num
    elif math=='-':
        answer = f_num - s_num
    elif math=='*':
        answer = f_num * s_num
    elif math=='/':
        answer = f_num / s_num
       
    entry.insert(0, str(answer))
    

# Define the button
button_1 = Button(root, text="1",  padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2",  padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3",  padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4",  padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5",  padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6",  padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7",  padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8",  padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9",  padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0",  padx=20, pady=10, command=lambda: button_click(0))

button_ac = Button(root, text="CLEAR",  padx=33, pady=10, command=button_AC)
button_equal = Button(root, text='=', padx=47, pady=10, command=button_EQUAL)
button_add = Button(root, text='+', padx=18, pady=10, command=button_ADD)
button_substract = Button(root, text='-', padx=20, pady=10, command=button_SUBSTRACT)
button_multiply = Button(root, text='*', padx=20, pady=10, command=button_MULTIPLY)
button_divide = Button(root, text='/', padx=20, pady=10, command=button_DIVIDE)
button_dot = Button(root, text='.', padx=21, pady=10, command=lambda: button_DOT('.'))
button_zeros = Button(root, text='x1000', padx=8, pady=10, command=button_ZEROS)

# Put the buttons on the screen

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_zeros.grid(row=4, column=2)
button_equal.grid(row=4, column=3, columnspan=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=2, column=3)
button_substract.grid(row=2, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_divide.grid(row=1, column=4)
button_multiply.grid(row=1, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_ac.grid(row=3, column=3, columnspan=2)

root.mainloop()