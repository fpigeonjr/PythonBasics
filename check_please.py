import math

def split_check(num_people, total):
  return math.ceil(total / num_people)

total_due = float(input("What is the total? "))
total_people = int(input("How many people? "))
amount_due = split_check(total_people, total_due)

print("Each person owes ${}".format(amount_due))
