"""
Instuctions:
You've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
- Small pizza (S): $15
- Medium Piza (M): $20
- Large Pizza (L): $25
- Add pepperoni for small pizza (Y or N): +$2
- Add pepperoni for medium / large pizza (Y or N): +$3
- Add extra cheese for any size pizza (Y or N): +$1 
"""

def order_pizza():
  print("Thank you for chosing Python Pizza Deliveries!")
  bill = 0
  size = input("What size pizza do you want (S/M/L)? \n> Your answer: ")
  add_pepperoni = input("Do you want pepperoni? (Y / N)\n> Your answer: ")
  if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
      bill += 2
    else:
      bill
  elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
      bill += 3
    else:
      bill
  elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
      bill += 3
    else:
      bill
  
  extra_cheese = input("Do you want extra cheese? (Y / N)> Your answer: ")
  if extra_cheese == 'Y':
    bill += 1
  
  return bill


if __name__ == "__main__":
  bill = order_pizza()
  print(f"Your final bill is ${bill}")
  