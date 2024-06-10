def price_calculator(height):
  """_summary_

  Args:
      height (int): the height of the visitor
  """
  
  bill = 0
  if height >= 120:
    print("Yes, you can ride!")
    
    age = int(input("Please input your age: "))
    
    if age < 12: 
      print("Child tickets are $5")
      bill += 5
    elif age <= 18: 
      print("Youth tickets are $7")
      bill += 7
    else:
      print("Adult tickets are $12")
      bill += 12
    
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == 'Y':
      bill += 3
      
    print(f"Your final bill is ${bill}")
    
  else:
    print("Oh no, you can't ride.")
  

height = int(input("Please input your height (in cm): "))
price_calculator(height)



  