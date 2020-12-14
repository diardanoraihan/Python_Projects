# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:10:09 2020

@author: Diardano Raihan
"""

def drawField(field):
    print('\n0 1 2 3 4 5 6')
    for row in range(11): # 0,1,2,3,4,...,10
                          # 0,.,1,.,2,..
        if row%2==0: #0,2,4,..
            practicalRow = int(row/2) # 0,1,2,..
            for column in range(13): # 0,1,2,3,4,...,12
                                     # 0,.,1,.,2,.
                practicalCol = int(column/2)
                if column%2==0:
                    if column!=12:
                        print(field[practicalRow][practicalCol], end='')
                    else:    
                        print(field[practicalRow][practicalCol])
                else:
                    print('|', end='')

        else:
            print('-------------')
