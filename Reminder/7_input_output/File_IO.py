# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 08:46:52 2020

@author: Diardano Raihan
"""

VacationSpots=['Bandung', 'Jakarta', 'Bogor', 'Palembang', 'Pekanbaru']

# Automatically this will create a new file called VacationPlaces

with open('VacationPlaces', 'w') as file:
    for spot in VacationSpots:
        file.write(spot + '\n')
        
with open('VacationPlaces', 'r') as file:
    name = file.read()
    
print(name)

FinalSpot = 'Thailand'

with open('VacationPlaces', 'a') as file:
    file.write(FinalSpot)

with open('VacationPlaces', 'r') as file:
    for place in file:
        print(place, end='')

#VacationFile = open(VacationPlaces,'w)
#    for spot in VacationSpots:
#        VacationFile.write(spot + '\n')
#    