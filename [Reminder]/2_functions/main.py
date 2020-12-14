"""
Title: Homework Assignment #2: Functions
Details: Create a file containing 3 functions from 3 specified song attributes
"""

# Defining three functions with the same name as the song attributes
def artist():
    return "Muse"

def song():
    return "Time is Running Out"

def year():
    return 2003

def isItBand(): # Extra function to identify the artist is a group band
    return True

# Calling the functions
Artist = artist()
Song = song()
Released = year()
isBand = isItBand()

# Print the attributes
print(Artist)
print(Song)
print(Released)
print(isBand)
