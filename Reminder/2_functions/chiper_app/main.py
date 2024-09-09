from misc import txtEncoder, txtDecoder

game_over = False
while not game_over:
  userChoice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  while userChoice not in ['encode', 'decode']:
    print('Your input is not valid!')
    userChoice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  
  if userChoice == 'encode':
    txt2encode = input("Type your message to encode:\n")
    shift = int(input("Type the shift number:\n"))
    txtEncoder(txt2encode, shift)
    
  elif userChoice == 'decode':
    txt2encode = input("Type your message to decode:\n")
    shift = int(input("Type the shift number:\n"))
    txtDecoder(txt2encode, shift)

  isContinue = (input("Type 'yes' if you want to continue again. Otherwise, type 'no'.\n")).lower()
  while isContinue not in ['yes', 'no']:
    print('Your input is not valid!')
    isContinue = (input("Type 'yes' if you want to continue again. Otherwise, type 'no'.\n")).lower()

  if isContinue == 'yes':
    game_over = False
  elif isContinue == 'no':
    game_over = True

