# Level: Easy

def bmi_calculator(height, weight):
  result = weight / (height**2)
  return result

height = float(input("Enter your height in meters e.g., 1.73: "))
weight = int(input("Enter your weight in Kg e.g., 70: "))
bmi = bmi_calculator(height, weight)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")