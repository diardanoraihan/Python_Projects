"""
Title:
Homework Assignment #7: Dictionaries and Sets
"""

dict_song = {'artist':'Muse',
             'song': 'Time is Running Out',
             'album': 'Absolution',
             'genre': 'Alternative Rock',
             'year': 2003,
             'label':'East West',
             'durationinseconds':241,
             'durationinminutes':4.01667}

for key in dict_song:
    # In a single loop, print its keys and its values
    print('{}: {}'.format(key,dict_song[key]))


# --------------- Extra Credit ----------------
def guessKeyValue(key,value):
    if key in dict_song:
        if dict_song[key]==value:
            # print('True')
            return True
        else:
            return False
    else:
        # print('False')
        return False

"""
# Debugging Purpose
guess = guessKeyValue('artist', 'Muse')
print(guess) # Print True
guess = guessKeyValue('year', 2003)
print(guess) # Print True
guess = guessKeyValue('artist', 'Radiohead')
print(guess) # Print False
guess = guessKeyValue('band', 'Muse')
print(guess) # Print False
"""

special_keys = ['year', 'durationinseconds', 'durationinminutes']

key = input('What is the key: ')
if key not in special_keys:
    value = input('What is the value: ')
    guess =  guessKeyValue(key, value)
    print(guess)
else:
    value = int(input('What is the value: '))
    guess = guessKeyValue(key, value)
    print(guess)
