# Regular If Statement
def numberChecker(n):
  if n % 2 == 0:
    print('Your number is even!')
  else:
    print('Your number is odd!')

inputNumber = int(input('Check if your number is even or odd: '))
numberChecker(inputNumber)

# Nested If Statement
height = int(input("Please input your height: "))
if height >= 120:
  print("Yes, you can ride!")
  age = int(input("Please input your age: "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("Oh no, you can't ride.")




