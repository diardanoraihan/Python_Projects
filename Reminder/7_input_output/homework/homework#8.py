# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:50:49 2020

@author: Diardano Raihan

Title: Homework Assignment #8: Input and Output (I/O)

"""

# We will use the pathlib module -> pathlib.Path.exists()

import pathlib
#import os
status = True

def printList(textlist):
    for line in textlist:
        print(line.strip('\n'))

while status:

    inputFile = input('Enter the name text file : ') + '.txt'
    path = pathlib.Path(inputFile)
    #print(inputFile)
    
    
    if path.exists():
        print('The file you access: {}'.format(inputFile))
        print('A) Read the file')
        print('B) Delete the file and start over')
        print('C) Append the file')
        print('D) Replace a single line')
        print('E) Exit')
        
        action = str(input('Please choose the action: ')).lower()
        
        if action =='a':
            fileName = open(inputFile, 'r')
            print(fileName.read())
            fileName.close()
            
        elif action =='b':
            print('{} is deleted. This file will start over '.format(inputFile))
            fileName = open(inputFile, 'w')
            fileName.write('')
            fileName.close()

        elif action =='c':
            fileName = open(inputFile, 'a')
            newText = input('Add new text here: ') + '\n'
            fileName.write(newText)
            fileName.close()
            
        elif action =='e':
             status = False
            
        elif action =='d':
            fileName = open(inputFile, 'r')
            textList = fileName.readlines()  # return list of text per line
            # ex: ['textLine 1\n', 'textLine 2\n', 'textLine 3\n']
            fileName.close()
            
            printList(textList)
            
            print('Please enter the line number you want to update', end='')
            lineNumber = int(input('Choose between {}-{}: '.format(0, len(textList)-1)))
            while lineNumber>=len(textList):
                print('Action failed!!!', end ='')
                lineNumber = int(input('Choose between {}-{}: '.format(0, len(textList)-1)))
            
            newText = input('Please add the new text for line {}: '.format(lineNumber))
            textList[lineNumber] = newText +'\n'
            
            with open(inputFile, 'w+') as fileName:
                for line in textList:
                    fileName.write(line)
            printList(textList)
                    
    else:         
        print('You create a new file: {}'.format(inputFile))
        fileName = open(inputFile, 'w') # open note_math.txt with write mode
        fileName.write(input('Enter the text here: '))
        fileName.write('\n')
        fileName.close()
    