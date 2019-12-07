# ===========================================
# Title: Exercise 8.3
# Author: Cory Gilliam
# Date: 7 Dec 2019
# Modified By:
# Description: Python Calculator
# ===========================================

# Add two numbers together
def add(intOne, intTwo):
  return intOne + intTwo

# Subtract a number for another number
def subtract(intOne, intTwo):
  return intOne - intTwo

# Divide a number by a second number, Neither number being zero
def divide(intOne, intTwo):
  if intOne != 0 and intTwo != 0:
    return intOne / intTwo
  else:
    return str(intOne) + " / " + str(intTwo) + " is not defined."

# Print results of function calls
print(add(1, 2))
print(subtract(4, 1))
print(divide(8, 2))
