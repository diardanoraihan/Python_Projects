# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:47:00 2020

@author: Diardano Raihan
"""

n = int(input())
for i in range(n):
    string=input()
    front = ''
    back = ''
    for i in range(len(string)):
        if i%2==0:    
            front += string[i]
        else:
            back += string[i]

    full = front + ' ' + back
    print(full)


  
#def print_to_stdout(*a): 
#  
#    # Here a is the array holding the objects 
#    # passed as the arguement of the function 
#    print(*a, file = sys.stdout) 
#  
#print_to_stdout("Hello World") 