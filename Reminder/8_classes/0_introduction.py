# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 07:47:41 2020

@author: Diardano Raihan

Classes are a form of object that has certain properties and attributes that go
together. This is something that you can create and save for later.

The properties of classes are:
    - They have their own variables
    - They have their own descriptions
    - They have their own functions called 'Methods'
    - They have certain attributes 
    - They can do certain things
    

"""

# Define a class name
# class className:
#
#     Create a function(s) inside the class that initializes all attributes
#     The attribute inside the __init__() function is called 'self' because
#     when we interact with it, it always has to interact with it 'self'.
#
#    def __init__(self):
#         We create an attribute (variable) that belongs to the class
#        self.Attribute = 0
#         Using self(dot) makes the Attribute variable an attribute of the class
#
#     define the class method (function)
#    def anotherFunc(self, param1, param2):
#        self.Attribute = param1
#        Action(s)

        
class Team: 

#    def __init__(self):
#        self.TeamName = "Name" # default value for TeamName
#        self.TeamOrigin = "Origin" #  default value for TeamOrigin

    def __init__(self, Name = "Name", Origin="Origin"):
        self.TeamName = Name # default value for TeamName
        self.TeamOrigin = Origin #  default value for TeamOrigin
        
    def defineTeamName(self, Name):
        self.TeamName = Name
        
    def defineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin
        

# We instantiate the Team()
Team1 = Team("Tigers", "Chicago")
# We create an instance here called Team1
# Instance is an individual object of a certain class, this case, Team class
Team2 = Team("Hawks", "New York")

Team3 = Team()

print(Team1)
print(Team1.TeamName)
Team1.defineTeamName("Dolphins")
print(Team1.TeamName)

print(Team1.TeamOrigin)
Team1.defineTeamOrigin("Chicago")
print(Team1.TeamOrigin)

print(Team2.TeamName)
print(Team2.TeamOrigin)

print(Team3.TeamName)
print(Team3.TeamOrigin)


        
        
        
        
        
        
        
        
        
        