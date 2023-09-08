# IMPLEMENT A RECURSIVE FUNCTION TO CALCULATE THE FACTORIAL OF A GIVEN NUMBER.

def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)


for i in range(10):
   print(factorial(i))