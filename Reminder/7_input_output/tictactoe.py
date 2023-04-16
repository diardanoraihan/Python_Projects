# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 09:15:27 2020

@author: Diardano Raihan
"""

# | |
#-----
# | |
#-----
# | |


def drawField(field):
    for row in range(5): #0,1,2,3,4
                         #0,.,1,.,2
        if row%2==0: #0,2,4
            practicalRow = int(row/2) #0,1,2
            for column in range(5): #0,1,2,3,4
                                    #0,.,1,.,2
                if column%2==0: #0,2,4
                    practicalColumn = int(column/2) #0,1,2
                    if column!=4:
                        print(field[practicalColumn][practicalRow], end='')
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print('|', end='')
        else:
            print('-----')

player = 1
#currentField = [column0, column1, column2]
currentField = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
drawField(currentField)
while(True):
    print('Players turn: ', player)
    MoveRow = int(input('Please enter the row: '))
    MoveColumn = int(input('Please enter the column: '))
    if player ==1:
        #make move for player 1
        if currentField[MoveColumn][MoveRow]==' ':
            currentField[MoveColumn][MoveRow] = 'X'
            player = 2
        
    else:
        #make move for player 2
        if currentField[MoveColumn][MoveRow]==' ':
            currentField[MoveColumn][MoveRow] = 'O'
            player=1
    drawField(currentField)