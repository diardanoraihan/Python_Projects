# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:26:17 2020

@author: Diardano Raihan
"""

def checkRow(field):
    list_Reps =[]
    for row in range(6):
        count = 1
        for col in range(1,7):
            if field[row][col-1]==field[row][col]:
                count+=1
                
            else:
                list_Reps.append((field[row][col-1], count))               
                count = 1
                
        list_Reps.append((field[row][col], count))
#    print(list_Reps)
    if ('O',4) in list_Reps or ('X',4) in list_Reps:
        return True
    else:
        return False

#currentField = [[' ','X',' ','O',' ','O','O'],
#                [' ','X',' ','O',' ','X',' '],
#                ['X','X','O','O','O','O','O']]
#
#result = checkRow(currentField)
#print(result)



def checkCol(field):
    list_Reps = []
    for col in range(7):
        count = 1
        for row in range(1,6):
            if field[row-1][col]==field[row][col]:
                count+=1
            else:
                list_Reps.append((field[row-1][col], count))
                count=1
        list_Reps.append((field[row][col], count))
#    print(list_Reps)
    if ('O',4) in list_Reps or ('X',4) in list_Reps:
        return True
    else:
        return False

#currentField = [[' ','X',' ','O',' ','O','O'],
#                [' ','X',' ','O',' ','X',' '],
#                ['X','X','O','O','O','O','O']]
#
#result = checkCol(currentField)
#print(result)

#def checkDiag(field):
#    list_Reps = []
#    count=1
#    for i in range(1,3):
#        if field[i-1][i-1]==field[i][i]:
#            count+=1
#        else:
#            list_Reps.append((field[i-1][i-1], count))
#            count=1
#    list_Reps.append((field[i][i], count))
#    print(list_Reps)

# Descending Diagonal
def checkDescDiag(field):
    cond = False
    for col in range(4):
        for row in range(3):
            if field[row][col]==' ':
                continue
            
            if field[row][col]==field[row+1][col+1]==field[row+2][col+2]==field[row+3][col+3]:
                cond = True
                # print('mycond ',cond)
                break
    return cond
            
# Ascending Diagonal
def checkAscDiag(field):
    cond = False
    for col in range(-1, -5,-1):
        for row in range(3):
            if field[row][col]==' ':
                continue
        
            if field[row][col]==field[row+1][col-1]==field[row+2][col-2]==field[row+3][col-3]:
                cond = True
                # print('mycond ',cond)
                break
    return cond            

            

#                      |           |
#currentField = [['O','X',' ','O','X','O','O'],
#                [' ','X',' ','X',' ','O',' '],
#                ['X','X','X','O','O','O','O'],
#                ['X','O',' ','X',' ','O','O'],
#                [' ','X','X','O','X','X',' '],
#                ['X','X','O','O','O','O','O']]
#
#print(checkDescDiag(currentField))
#print(checkAscDiag(currentField))
#print(result)

