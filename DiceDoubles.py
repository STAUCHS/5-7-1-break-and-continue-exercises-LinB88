#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
import random

# Header
print("HERE COMES THE DICE!")

# initialize variables and random

roll_1 = random.randrange(1,7)
roll_2 = random.randrange(1,7)

# loop if roll is different
while roll_1 != roll_2:
    print(f"Roll #1: {roll_1}")
    print(f"Roll #2: {roll_2}")
    sum = roll_1 + roll_2
    print(f"The total is {sum}!")
    roll_1 = random.randrange(1,7)
    roll_2 = random.randrange(1,7)
    
# If roll is same
    if roll_1 == roll_2:
        print(f"Roll #1: {roll_1}")
        print(f"Roll #2: {roll_2}")
        sum = roll_1 + roll_2
        print(f"The total is {sum}!")