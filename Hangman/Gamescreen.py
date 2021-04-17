import time

# Define a HangMan class
# This class is responsible for:
# - a user's current game status (How many times the user falsely guess the letter)
# - drawing the gallow based on user's status on the screen
class HangMan:
    def __init__(self, stat=1):
        # status represents the number of wrong guesses by a user
        # initialize its value by zero
        # and 8 is the maximum status number indicating
        # the hangman drawing is complete
        self.status = stat

    def addFalse(self, false=True):
        if false==True:
            self.status +=1


    def Show(self):
        # g_i represents the gallow condition for the user to pay attention
        g_1 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        g_2 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        g_3 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551      \u257D",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        g_4 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551     \u2571\u257D",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        g_5 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551     \u2571\u257D\u2572",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        g_6 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551     \u2571\u257D\u2572",
               "\t\t\t\t\t   \u2551     \u2571",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        g_7 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551     \u2571\u257D\u2572",
               "\t\t\t\t\t   \u2551     \u2571 \u2572",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        # Complete the hangman drawing
        g_8 = ["",
               "\t\t\t\t\t   \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2555",
               "\t\t\t\t\t   \u2551      \u2502",
               "\t\t\t\t\t   \u2551      @",
               "\t\t\t\t\t   \u2551     \u2571\u257D\u2572",
               "\t\t\t\t\t   \u2551     \u2571 \u2572",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t   \u2551",
               "\t\t\t\t\t\u2554\u2550\u2550\u2569\u2550\u2550\u2557",
               ""]

        # Store the gallow drawing in the form of a dictionary
        gallow = {1: g_1, 2: g_2, 3: g_3, 4: g_4, 5: g_5, 6: g_6, 7: g_7, 8: g_8}

        for row in gallow[self.status]:
            print(row)

# The Fields class is responsible for:
# - obtain a word to be guessed by the user
# - drawing fields for the user to fill in with a guessed letter
# - updating the fields each time user correctly guess the letter
class Fields:
    def __init__(self, word="test"):
        self.length = len(word)
        self.word = []
        for i in range(self.length):
            self.word.append(word[i])
        self.field = []
        for i in range(self.length):
            self.field.append("_")

    def updateField(self, guess):
        # Update the field with the correct guesses
        false = False
        if guess in self.word:
            indices = [idx for idx, letter in enumerate(self.word) if letter == guess]
            for index in indices:
                self.field[index] = guess

        # Otherwise, give a flag that this guess is falsse
        else:
            false = True

        return false

    def checkField(self):
        if "_" not in self.field:
            return True
        else:
            return False

    def Show(self):
        print("Guess the word\t: ", end="")
        for i in self.field:
            print(i, end=' ')

# ------------------------------- Debugging the code -----------------------------#
# test = HangMan()
# print(test.status)
# test.addFalse()
# print(test.status)
# test.Show()
# test.addFalse()
# print(test.status)
# test.Show()

# for i in range(len(g_1)):
#     print(g_1[i], end=' ')

# test = Fields('ayaappaapap')
# print(test.word)
# print(test.field)
# # for i in test.field:
# #     print(i, end=' ')
# a = test.updateField('a')
# test.Show()
# print(a)
# a = test.updateField('p')
# test.Show()
# print(a)