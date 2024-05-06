#-------------------------------------------------------------------------
# Name:       Adds numbers from 5 to 20 but not multiples of 3
# Purpose:    adds numbers.
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

num = 5
total = 0

while num in range(5,21):
    if num % 3 != 0:
        total += num
    num += 1

print(total)