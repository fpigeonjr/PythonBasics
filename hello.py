first_name = input("What is your first name? ")
print("Hello, ", first_name)

if first_name == "Frank":
  print(first_name, "is learning Python!")
  print(first_name + " is the best!")
elif first_name == "Max":
  print(first_name + " is learning Python with the community.")
else: 
  age = int(input("How old are you? "))
  # just in case have a younger user who can't read
  if age <= 6 :
    print("Maybe you should learn to read first!")
  else :
    print("You should totally learn Python {}".format(first_name))

print("Have a great day {}".format(first_name))
# print("Hello Frank")
# print("Hello,",first_name)
# print("Frank is learning Python.")
# print(first_name, "is learning Python")

