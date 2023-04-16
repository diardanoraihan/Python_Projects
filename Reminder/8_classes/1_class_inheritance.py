# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:40:36 2020

@author: Diardano Raihan

Class inheritance:
- is a sub section of a bigger class;
- lets us access all the new methods and the old methods in
the parent class.

Since our Inheritance Class or sub class inherits some properties
some properties from the parent class, we need to initialize it by calling
the initializer of the ParentClass (line 41)
"""
#class className:
    
#    def __init__(self):
#        self.Attribute = 0
        
#    def anotherFunc(self):
#        Action(s)



class Team: 

    def __init__(self, Name = "Name", Origin="Origin"):
        self.TeamName = Name # default value for TeamName
        self.TeamOrigin = Origin #  default value for TeamOrigin
        
    def defineTeamName(self, Name):
        self.TeamName = Name
        
    def defineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin
        
#class InheritanceClassName(ParentClass):
#    
#    def __init__(self, Input1, Input2):
#        ParentClass.__init__(self)
#        self.Attribute1 = Input1
#        self.Attribute2 = Input2
#        self.Attribute3 = 0
#    
#    def AnotherMethod(self):
#        Action(s)
        
class Player(Team):
    def __init__(self, pName, pPoints, teamName, teamOrigin):
        Team.__init__(self, teamName, teamOrigin)
        self.playerName = pName
        self.playerPoints = pPoints
    
    def scoredPoint(self):
        self.playerPoints +=1
        
    def setName(self, Name):
        self.playerName = Name
    
    # Custom output by overwriting the string
    def __str__(self): # allows us to call the instance and return a certain message (line 74)
        return self.playerName + " has scored: " + str(self.playerPoints) + " points"
    
player1 = Player("Sid", 0, "Sharks", "Chicago")
print(player1.playerName)
print(player1.playerPoints)
#player1.defineTeamName("Sharks")
# Something cool about inheritance class is that you can call the attributes
# of your parent class
print(player1.TeamName)
print(player1.TeamOrigin)

player1.scoredPoint()
print(player1.playerPoints)

player1.setName("Lee")
print(player1.playerName)

# Print the string that we set in __str__ method
print(player1)
            