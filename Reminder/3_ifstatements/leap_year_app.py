# Level: Intermediate

def isLeapYear(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(f"Year {year} is a leap year!")
      else:
        print(F"Year {year} is NOT a leap year!")
    else:
      print(f"Year {year} is a leap year!")
  else:
      print(f'Year {year} is NOT a leap year!')

year = int(input("Enter a year: "))
isLeapYear(year)