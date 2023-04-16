"""
Title:
Homework Assignment #4: Lists
"""

# Define an empty list as a global variable
myUniqueList = []

# Create a function to add new element to the list
def addThings(thing):
    if thing not in myUniqueList:
        myUniqueList.append(thing)
        return True
    else:
        return False

# Test if the function works
# Add some new different elements to the list
print('Add \'First\', \'Second\', and int(3) as new elements to the myUniquelist')
addThings('First')
print(myUniqueList)

addThings('Second')
print(myUniqueList)

addThings(3)
print(myUniqueList)

# Test by adding an element that has been in the list already
print('Add \'First\' to myUniquelist again to check whether or not it appears twice')
addThings('First')
print(myUniqueList)
print('Add int(3) to myUniquelist again to check whether or not it appears twice')
addThings(3)
print(myUniqueList)
print('The function works on keeping the elements of myUniqueList unique')
