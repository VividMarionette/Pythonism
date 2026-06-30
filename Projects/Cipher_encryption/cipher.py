
message = input("Message: ")

shift = 3

encrypted = ""

for letter in message:
  encrypted += chr(ord(letter) + shift)

print("Encrypted: ", encrypted)
