# ===========================================
# Title: Exercise 8.3
# Author: Cory Gilliam
# Date: 7 Dec 2019
# Modified By:
# Description: Python Calculator
# ===========================================
def add(intOne, intTwo):
  return intOne + intTwo

def subtract(intOne, intTwo):
  return intOne - intTwo

def divide(intOne, intTwo):
  if intOne != 0 and intTwo != 0:
    return intOne / intTwo
  else:
    return str(intOne) + " / " + str(intTwo) + " is not defined."


print(add(1, 2))
print(subtract(4, 1))
print(divide(8, 2))
