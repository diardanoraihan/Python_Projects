# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:03:40 2020

@author: Diardano Raihan
"""
# ------------------- Part 1 -------------------

participantNumber = 3
participantData = []
registeredParticipants = 0
outputFile = open('ParticipantData.txt', "w")

while (registeredParticipants < participantNumber):
    tempPartData = [] #name, country of origin, age
    name = input('Please enter your name: ')
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: ")) # int('25') -> 25
    tempPartData.append(age) # [name, country, age]
    
#    print(tempPartData)
    participantData.append(tempPartData) 
#    print(participantData)
    #[tempPartData] = [[name, country, age], [..]]
    registeredParticipants +=1 # = registeredParticipants + 1
    
for participant in participantData:
    for data in participant:
        outputFile.write(str(data)) # str(25) -> "25"
        outputFile.write(" ") # Diar Indonesia 26
                              # Bob Canada 23
    outputFile.write("\n")    

outputFile.close()

# ------------------- Part 2 -------------------

inputFile = open('ParticipantData.txt', 'r')

inputList = []

for line in inputFile:
    # "Diar Indonesia 26 \n".strip("\n") -> "Diar Indonesia 26 "
    # "Diar Indonesia 26 ".split() -> ["Diar", "Indonesia", "26"]
    # split() will split the sentence into words by white space
    tempParticipant = line.strip("\n").split()
#    print(tempParticipant)
    inputList.append(tempParticipant)
#    print(inputList)

Age = {}
print(inputList)
for part in inputList:
    tempAge = int(part[-1]) # int('21') -> 21
    if tempAge in Age:
        Age[tempAge]+=1
    else:
        Age[tempAge]=1
        
print(Age)

# ------------------- Part 3 -------------------
Countries = {}
for part in inputList:
    tempCountry = part[1] # int('21') -> 21
    if tempAge in Countries:
        Countries[tempCountry]+=1
    else:
        Countries[tempCountry]=1

print("Countries that attended:",Countries)

oldest = 0
youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
    if tempAge > oldest:
        oldest = tempAge
    if tempAge<youngest:
        youngest = tempAge
    if Age[tempAge]>=counter:
        counter = Age[tempAge]
        mostOccuringAge = tempAge
        
        
print(oldest)
print(youngest)
print("Most occuring age is:", mostOccuringAge, "with", counter, "participant")
inputFile.close()

        
    
