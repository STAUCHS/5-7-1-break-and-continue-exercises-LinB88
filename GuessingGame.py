#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
import random
# Generate random number between 1 and 100
num = random.randrange(1, 101)

# Get guess from user
guess = int(input("Enter a number between 1 and 100: "))

tries = 1

# When guess is incorrect
while guess != num and tries < 5:
  if guess > num:
    print("Guess is too high. Guess again.\n")
  else:
    print("Guess is too low. Guess again.\n")
    
  guess = int(input("Enter a guess: "))
  tries += 1

# Output message when guess is correct
if tries < 5:
  print("Congratulations! You guessed correct!")

# Output message when guess is incorrect and number of tries is used up
else:
  print(f"Sorry! Game Over! The number was {num}.")
