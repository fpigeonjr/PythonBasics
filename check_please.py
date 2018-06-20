import math

def split_check(num_people, total):
  if num_people <= 1:
    raise ValueError("More than one person is required to split the check ")
  return math.ceil(total / num_people)

try:
  total_due = float(input("What is the total? "))
  total_people = int(input("How many people? "))
  amount_due = split_check(total_people, total_due)
except ValueError as err:
  print("Oh no! That's not a valid value.")
  print("{}".format(err))
else:
  print("Each person owes ${}".format(amount_due))
