encryptedMessage = "kwwsv://grfv.jrrjoh.frp/grfxphqw/g/1ZjRoJR9YvcU0vyTfFJMtfinkKe1ihL05kClJ7VQFnQL/hglw?xvs=vkdulqj"

decryptedMessage = ""

for letter in encryptedMessage:
  if letter.isalpha():
    letter_shifted = chr((ord(letter) - 3 - ord('a')) % 26 + ord('a'))
  else:
    letter_shifted = letter
    
  decryptedMessage += letter_shifted

print(decryptedMessage)