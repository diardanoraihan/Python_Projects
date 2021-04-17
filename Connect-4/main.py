# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 07:32:50 2020

@author: Diardano Raihan
"""

# | | | | | | 
#-------------
# | | | | | | 
#-------------
# | | | | | | 
#-------------
# | | | | | | 
#-------------
# | | | | | | 
#-------------
# | | | | | | 

from winCheck import checkRow, checkCol, checkAscDiag, checkDescDiag
from utilities import drawField

def isRowFull(): 
    if 0<=moveCol<=6:
        for row in range(-1,-7,-1):
            if currentField[row][moveCol]!=' ' and row!=-6:
                continue
            elif currentField[row][moveCol]!=' ' and row==-6:
                candidateRow = -7
                break
            else:
                candidateRow = row
                break
    else:
        candidateRow = -7
    return candidateRow

# initiate the game
print('Welcome to the Connect 4 Game!')
currentField = [[' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ']]
player = 1
drawField(currentField)
finished = False

# Run the game
while (finished!=True):
    moveCol = int(input('Player {} chooses column: '.format(player)))
    moveRow = isRowFull()
    if 0<=moveCol<=6 and -6<=moveRow<=-1:
        if player==1:
            #make move for player 1
            if currentField[moveRow][moveCol]==' ':
                currentField[moveRow][moveCol] = 'X'
                player = 2
            
        else:        
            #make move for player 1
            if currentField[moveRow][moveCol]==' ':
                currentField[moveRow][moveCol] = 'O'
                player = 1
                
        drawField(currentField)
        if checkRow(currentField) or checkCol(currentField) or checkDescDiag(currentField) or checkAscDiag(currentField):
            finished=True
    else:
        print('Wrong Column!!')


# Closing the game
if player==1:
    print('Congratulations!!!')
    print('The winner is player {}'.format(player+1))
else:
    print('Congratulations!!!')
    print('The winner is player {}'.format(player-1))    
        

#
#    
    
            

                