# LEAP YEAR

def is_leap_year(year):
  if(year%4==0 and year%100!=0)or(year%400==0):
    return True
  else:
    return False

# GET INPUT FROM THE USER

user_year=int(input("ENTER A YEAR:"))

#CHECK IF IT'S A LEAP YEAR

if is_leap_year(user_year):
  print(f"{user_year}is a leap year.")
else:
  print(f"{user_year}is not a leap year.")