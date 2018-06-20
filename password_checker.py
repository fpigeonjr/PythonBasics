import sys

attempt_count = 1
MASTER_PASSWORD = "password123"

password = input("Please enter your password: ")

while password != MASTER_PASSWORD:
  if attempt_count > 3:
    sys.exit("Too many password attempts")
  password = input("Invalid Password, try again: ")
  attempt_count += 1

print("Password unlocked!")