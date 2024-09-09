letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def txtEncoder(message, shift):
  idx2encode = []
  for txt in message:
    idx2encode.append(letters.index(txt))

  final_indices = []
  for idx in idx2encode:
    if (idx + shift) < 26:
      new_idx = idx + shift
    else:
      new_idx = (idx + shift) - 26
    final_indices.append(new_idx)

  txtEncoded = ""
  for idx in final_indices:
    txtEncoded += letters[idx]
  
  print(txtEncoded)

def txtDecoder(message, shift):
  idx2decode = []
  for txt in message:
    idx2decode.append(letters.index(txt))

  final_indices = []
  for idx in idx2decode:
    new_idx = idx - shift
    final_indices.append(new_idx)

  txtDecoded = ""
  for idx in final_indices:
    txtDecoded += letters[idx]
  
  print(txtDecoded)
  