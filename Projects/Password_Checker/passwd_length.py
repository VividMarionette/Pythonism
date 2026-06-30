
password = input("Enter your password: ")

if len(password) <4:
  print("Password is too short")

elif len(password) <6:
  print("Password is near")

else:
  print("Strong Password")
