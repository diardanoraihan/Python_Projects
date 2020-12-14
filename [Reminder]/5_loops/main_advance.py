"""
Title:
Homework Assignment #6: Advanced Loops
"""

def funct(rows, columns):
    if rows<9 and columns<9: # Maximum integer inputs allowed
        for i in range(rows): # Rows
            if i%2==0: # For even rows
                for j in range(columns): # Columns
                    if j%2==0 and j<columns-1: # For even columns not at the edge
                        print(" ", end='')
                    elif j%2!=0 and j<columns-1: # for odd columns not at the edge
                        print('|', end='')
                    elif j%2==0 and j==columns-1: # for even column at the edge
                        print(" ")
                    elif j%2!=0 and j==columns-1: # for odd column at the edge
                        print("|")

            else: # For odd rows
                for j in range(columns):
                    if j<columns-1:
                        print("-", end='')
                    else:
                        print("-")
        return True
    else:
        return False

# Call the function which it return True
funct(5,5)
funct(7,8)
funct(6,8)
# Call the function which it return False
funct(9,10)
