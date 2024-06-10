def love_calculator(name_1, name_2):
  name_combined = name_1 + name_2
  name_combined = name_combined.lower()
  true_count = ['t', 'r', 'u', 'e']
  love_count = ['l', 'o', 'v', 'e']
  true_score = 0
  love_score = 0
  for letter in true_count:
    true_score += name_combined.count(letter)
  for letter in love_count:
    love_score += name_combined.count(letter)
  
  result = int(str(true_score) + str(love_score))
  
  if (result < 10) or (result > 90):
    print(f"Your score is {result}, you go together like coke and mentos.")
  elif (result >= 40) and (result <= 50):
    print(f"Your score is {result}, you are alright together.")
  else:
    print(f"Your score is {result}.")

if __name__ == "__main__":
  name_1 = input()
  name_2 = input()

  love_calculator(name_1, name_2)
  