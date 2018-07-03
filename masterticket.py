TICKET_PRICE = 10
tickets_remaining = 100

# run this code while we have tickets

while tickets_remaining :

  # output how many tickets are available

  print("There are {} tickets remaining".format(tickets_remaining))

  # gather user's name and assign it to a new variable

  name = input("Please input your name? ")
  print("Welcome, {}".format(name))

  # prompt user by name how many tickets they would like to purchase
  num_tickets = int(input("How many tickets would you like to purchase {}? ".format(name)))
  while num_tickets > tickets_remaining :
    print("There are not that many tickets available. Please try again")
    num_tickets = int(input("How many tickets would you like to purchase {}? ".format(name)))

  # calculate the price
  def calculate_price(num_tickets) :
    return num_tickets * TICKET_PRICE

  # output the price
  print("Your total will be ${}".format(calculate_price(num_tickets)))

  # prompt user is they want to continue Y/N
  confirm = input("Would you like to continue? Y/N ").upper()

  # if yes, print out SOLD
  if confirm == "Y" :
    # decrement tickets remaining
    tickets_remaining -= num_tickets
    print("SOLD!")
  # if no, thank them by name
  else :
    print("Thank you anyways {}".format(name))

  print('\n\n')
# if there are no more tickets, print SOlD OUT
print ("Sold Out!!!")