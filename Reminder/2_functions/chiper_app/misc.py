letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def txtEncoder(message, shift):
  message = message.lower()
  idx2encode = []
  for txt in message:
    if txt in letters:
        if letters.index(txt) + shift < 26:
          idx2encode.append(letters.index(txt) + shift)
        else:
          idx2encode.append(letters.index(txt) + shift - 26)
    else:
      idx2encode.append(txt)

  txtEncoded = ""
  for idx in idx2encode:
    if isinstance(idx, int):
      txtEncoded += letters[idx]
    else:
      txtEncoded += idx

  print(txtEncoded)

def txtDecoder(message, shift):
  message = message.lower()
  idx2decode = []

  for txt in message:
    if txt in letters:
      idx2decode.append(letters.index(txt) - shift)
    else:
      idx2decode.append(txt)

  txtDecoded = ""
  for idx in idx2decode:
    if isinstance(idx, int):
      txtDecoded += letters[idx]
    else:
      txtDecoded += idx

  print(txtDecoded)